#include <stdint.h>
#include <stdio.h>
#include "common.h"
#include "i2c_driver.h"

#define I2C_DRIVER_SCL_H GPIO_SetBits(GPIO_I2C_DRIVER, I2C_DRIVER_SCL)   // 拉高SCL时钟线
#define I2C_DRIVER_SCL_L GPIO_ResetBits(GPIO_I2C_DRIVER, I2C_DRIVER_SCL) // 拉低SCL时钟线
#define I2C_DRIVER_SDA_H GPIO_SetBits(GPIO_I2C_DRIVER, I2C_DRIVER_SDA)   // 拉高SDA数据线
#define I2C_DRIVER_SDA_L GPIO_ResetBits(GPIO_I2C_DRIVER, I2C_DRIVER_SDA) // 拉低SDA数据线

static void I2C_DRIVER_SDA_OUT(void);
static void I2C_DRIVER_SDA_IN(void);
static void I2C_DRIVER_Start(void);
static void I2C_DRIVER_Stop(void);
static void I2C_DRIVER_Ack(void);
static void I2C_DRIVER_NAck(void);
static u8   I2C_DRIVER_Wait_Ack(void);

//*****************I2C初始化函数*****************************************
void I2C_DRIVER_Init_GPIO(void)
{
  GPIO_InitTypeDef GPIO_InitStructure;                    // 定义结构体变量 
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);   // IIC时钟配置
  // RCC_APB2PeriphClockCmd(RCC_APB2Periph_AFIO, ENABLE); //打开第二功能，用于中断的使用
  /* 配置SCL线为推挽输出 ，配置SDA线为推挽输出 */
  GPIO_InitStructure.GPIO_Pin = I2C_DRIVER_SCL | I2C_DRIVER_SDA;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
  GPIO_Init(GPIO_I2C_DRIVER, &GPIO_InitStructure);
  //GPIO_PinRemapConfig(GPIO_Remap_SWJ_JTAGDisable, ENABLE); 
  //设置两线为高电平状态
  I2C_DRIVER_SCL_H;
  I2C_DRIVER_SDA_H;
}

//*****************I2C发送8个位一个字节的数据****************************
void I2C_DRIVER_Send_Byte(u8 txd)
{
  u8 i = 0;
  I2C_DRIVER_SDA_OUT();                                          // SDA为输出状态
  I2C_DRIVER_SCL_L;                                              // SCL拉低，开始数据传输
  for(i = 0; i < 8; i++)
  {
    if((txd & 0x80) > 0)
    {
      I2C_DRIVER_SDA_H;                                          // 0x80为10000000，屏蔽掉后面的7位数据，如果高位为高则值>0，且SDA置高
    }
    else
    { 
      I2C_DRIVER_SDA_L;                                          // SDA拉低
    }
    txd <<= 1;                                                   // 执行完第一次以后，左移一位，把第二位数据移到第一位进行同样的判断
    I2C_DRIVER_SCL_H;                                            // SCL置高
    delay_us(I2C_CYCLE_DELAY_US);                                // 延时I2C_CYCLE_DELAY_US微秒，发送数据
    I2C_DRIVER_SCL_L;                                            // SCL拉低，准备下一次发送
    delay_us(I2C_CYCLE_DELAY_US);                                // 延时I2C_CYCLE_DELAY_US微秒
  }   
}
//*****************I2C读取8个位一个字节的数据****************************
u8 I2C_DRIVER_Read_Byte(u8 ack)
{
  u8 i=0,receive=0;
  I2C_DRIVER_SDA_IN();  //SDA为输入状态
  /* ff：设置为输入状态后就不要设置状态了 */
  // I2C_DRIVER_SDA_H; 
  for(i = 0; i < 8; i++)
  {
    I2C_DRIVER_SCL_L;                                             // SCL拉低
    delay_us(I2C_CYCLE_DELAY_US);                                 // 延时I2C_CYCLE_DELAY_US微秒
    I2C_DRIVER_SCL_H;                                             // SCL置高
    receive <<= 1;                                                // 左移一位，存储数据
    if(GPIO_ReadInputDataBit(GPIO_I2C_DRIVER,I2C_DRIVER_SDA))   
    {
      receive++;//如果接收到数据，末位置1
    }
    delay_us(I2C_CYCLE_DELAY_US);                                 // 延时I2C_CYCLE_DELAY_US微秒
  }
  if(ack == 0)
  {
    I2C_DRIVER_NAck();                                            // 如果数据为0，不应答
  }
  else 
  {
    I2C_DRIVER_Ack();                                             // 如果数据为1，应答 
  }
return receive;                                                   // 返回数据               
}
//*****************I2C Read****************************//
void I2C_DRIVER_Read_Bytes(u8 SlaveAddress,u8 REG_Address, u8* rec_buffer, u8 len)
{   
  u8 temp = 0;    
  u8 i = 0;
  I2C_DRIVER_Start();   
  I2C_DRIVER_Send_Byte(SlaveAddress); 
  I2C_DRIVER_Wait_Ack(); 
  I2C_DRIVER_Send_Byte(REG_Address);  
  I2C_DRIVER_Wait_Ack(); 
  I2C_DRIVER_Start();
  I2C_DRIVER_Send_Byte(SlaveAddress + 1);
  I2C_DRIVER_Wait_Ack(); 
  for(i = 0; i < len - 1; i++)
  {
    *(rec_buffer + i) = I2C_DRIVER_Read_Byte(1);
  }
  *(rec_buffer + len -1)= I2C_DRIVER_Read_Byte(0);
  I2C_DRIVER_Stop();
}  
//*****************I2C Write******************************           
void I2C_DRIVER_Write_Bytes(u8 SlaveAddress, u8 REG_Address,u8* REG_data, u8 len)           
{
  u8 i = 0;
  I2C_DRIVER_Start();  
  I2C_DRIVER_Send_Byte(SlaveAddress);  
  I2C_DRIVER_Wait_Ack(); 
  I2C_DRIVER_Send_Byte(REG_Address);        
  I2C_DRIVER_Wait_Ack();    
  for(i = 0; i < len; i++)
  {
    I2C_DRIVER_Send_Byte(*(REG_data + i));
    I2C_DRIVER_Wait_Ack(); 
  }
   
  I2C_DRIVER_Stop(); 
  delay_ms(50);     
}

void I2C_DRIVER_POC(u8 SlaveAddress,u8 REG_Address,u8* REG_data, u8 len)           
{
  I2C_DRIVER_Start();  
  I2C_DRIVER_Send_Byte(SlaveAddress);  
  I2C_DRIVER_Wait_Ack(); 
  I2C_DRIVER_Send_Byte(REG_Address );        
  I2C_DRIVER_Wait_Ack();    

  I2C_DRIVER_Send_Byte(*(REG_data));
  I2C_DRIVER_Wait_Ack(); 
  I2C_DRIVER_Send_Byte(*(REG_data + 1));
  I2C_DRIVER_Stop(); 
  delay_ms(50);     
}


//*****************I2C_SDA输出方向函数***********************************
static void I2C_DRIVER_SDA_OUT(void)
{
  GPIO_InitTypeDef GPIO_InitStructure;                        //定义结构体变量
  GPIO_InitStructure.GPIO_Pin = I2C_DRIVER_SDA;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
  GPIO_Init(GPIO_I2C_DRIVER, &GPIO_InitStructure);
}

//*****************I2C_SDA输入方向函数***********************************
static void I2C_DRIVER_SDA_IN(void)
{
  GPIO_InitTypeDef GPIO_InitStructure;                           // 定义结构体变量
  GPIO_InitStructure.GPIO_Pin = I2C_DRIVER_SDA;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPU;
  GPIO_Init(GPIO_I2C_DRIVER, &GPIO_InitStructure); 
}

//*****************I2C起始信号函数***************************************
static void I2C_DRIVER_Start(void)
{
  I2C_DRIVER_SDA_OUT();                                          // SDA为输出状态 
  I2C_DRIVER_SDA_H;                                              // SDA置高
  I2C_DRIVER_SCL_H;                                              // SCL置高
  delay_us(I2C_CYCLE_DELAY_US);                                  // 延时I2C_CYCLE_DELAY_US微秒
  I2C_DRIVER_SDA_L;                                              // SDA拉低
  delay_us(I2C_CYCLE_DELAY_US);                                  // 持续时间I2C_CYCLE_DELAY_US微秒
  I2C_DRIVER_SCL_L;                                              // SCL拉低    
}

//*****************I2C终止信号函数***************************************
static void I2C_DRIVER_Stop(void)
{
  I2C_DRIVER_SDA_OUT();                                          // SDA为输出状态 
  I2C_DRIVER_SCL_L;                                              // SCL拉低
  I2C_DRIVER_SDA_L;                                              // SDA拉低
  I2C_DRIVER_SCL_H;                                              // SCL置高
  delay_us(I2C_CYCLE_DELAY_US);                                  // 延时I2C_CYCLE_DELAY_US微秒
  I2C_DRIVER_SDA_H;                                              // SDA置高
  delay_us(I2C_CYCLE_DELAY_US);                                  // 持续时间I2C_CYCLE_DELAY_US微秒
}
//*****************I2C主机产生应答信号函数*******************************
static void I2C_DRIVER_Ack(void)
{
  I2C_DRIVER_SCL_L;                                              // SCL拉低
  I2C_DRIVER_SDA_OUT();                                          // SDA为输出状态
  I2C_DRIVER_SDA_L;                                              // SDA拉低
  delay_us(I2C_CYCLE_DELAY_US);                                  // 延时2微秒
  I2C_DRIVER_SCL_H;                                              // SCL置高
  delay_us(I2C_CYCLE_DELAY_US);                                  // 延时I2C_CYCLE_DELAY_US微秒
  I2C_DRIVER_SCL_L;                                              // SCL拉低
}
//*****************I2C主机不产生应答信号函数*****************************
static void I2C_DRIVER_NAck(void)
{
  I2C_DRIVER_SCL_L;                                              // SCL拉低
  I2C_DRIVER_SDA_OUT();                                          // SDA为输出状态
  I2C_DRIVER_SDA_H;                                              // SDA置高
  delay_us(I2C_CYCLE_DELAY_US);                                  // 延时2微秒
  I2C_DRIVER_SCL_H;                                              // SCL置高
  delay_us(I2C_CYCLE_DELAY_US);                                  // 延时I2C_CYCLE_DELAY_US微秒
  I2C_DRIVER_SCL_L;                                              // SCL拉低
}
//*****************I2C等待从机应答信号函数*******************************
static u8 I2C_DRIVER_Wait_Ack(void)
{ 
  u8 tempTime=0;                                                 // 定义计数器
  /* 等待的应答信号又由芯片控制，不需要主动控制SDA，
   * 在SCL为高时读取SDA 状态上是否为高即可 */
  // I2C_DRIVER_SDA_H;                                           // SDA置高
  // delay_us(1);                                                // 延时1微秒
  I2C_DRIVER_SCL_H;                                              // SCL置高
  delay_us(I2C_CYCLE_DELAY_US); 
  I2C_DRIVER_SDA_IN();  //延时1微秒
  while(GPIO_ReadInputDataBit(GPIO_I2C_DRIVER,I2C_DRIVER_SDA))   // 读取SDA状态，为低则继续执行，为高则等待
  {
    tempTime++;                                            
    if(tempTime > 250)                                             // 计数器累加一定时间，证明没有接收到应答信号
    {              
      I2C_DRIVER_Stop();                                         // I2C停止工作
      return 1;                                                  // 返回数据1，表示接收数据失败
    }                                                            // 返回数据0，表示接收数据成功
  }
  I2C_DRIVER_SCL_L;                                              // SCL拉低
  return 0;
}
