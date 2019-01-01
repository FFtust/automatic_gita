#ifndef _I2C_DRIVER_H_
#define _I2C_DRIVER_H_

#include "GPIO_STM32F10x.h"

//**********************I2C宏定义*******************************
#define I2C_DRIVER_SCL   GPIO_Pin_4                // SCL时钟线
#define I2C_DRIVER_SDA   GPIO_Pin_15               // SDA数据线
#define GPIO_I2C_DRIVER  GPIOA                     // 使用B端口

#define I2C_FREQUENCY       (100000)
#define I2C_CYCLE_DELAY_US  (1000000 / I2C_FREQUENCY)

//**********************I2C函数申明******************************
void I2C_DRIVER_Init_GPIO(void);
void I2C_DRIVER_Send_Byte(u8 txd);
u8   I2C_DRIVER_Read_Byte(u8 ack);
void I2C_DRIVER_Read_Bytes(u8 SlaveAddress,u8 REG_Address, u8* rec_buffer, u8 len);
void I2C_DRIVER_Write_Bytes(u8 SlaveAddress,u8 REG_Address,u8* REG_data, u8 len);
void I2C_DRIVER_POC(u8 SlaveAddress,u8 REG_Address,u8* REG_data, u8 len);   

#endif /* _I2C_DRIVER_H_ */









