#include <stdint.h>
#include <stdio.h>
#include <math.h>
#include "common.h"
#include "i2c_driver.h"
#include "pca9685reg.h"
#include "pca9685_control.h"

static void PCA9685_write(u8 address, u8 data);
static void PCA9685_write_reg16(u8 address, u16 data);
static void PCA9685_read(char address, u8* rec_buffer, u8 len);

void pca9685_init(void)
{
  I2C_DRIVER_Init_GPIO();
  pca9685_set_freq(50);
}

void pca9685_set_freq(float freq)
{
  u8 prescale, oldmode, newmode;
  float prescaleval;
  freq *= 0.915; // Correct for overshoot in the frequency setTIng
  prescaleval = 25000000;
  prescaleval /= 4096;
  prescaleval /= freq;
  prescaleval -= 1;
  prescale = floor(prescaleval + 0.5);
  PCA9685_read(PCA9685_MODE1, &oldmode, 1);
  newmode = (oldmode & 0x7F) | 0x10; // sleep
	delay_ms(5);
  PCA9685_write(PCA9685_MODE1, newmode); // go to sleep
	delay_ms(5);
  PCA9685_write(PCA9685_PRESCALE, prescale); // set the prescaler
  prescale = 0;
  PCA9685_read(PCA9685_MODE1, &prescale, 1);
  PCA9685_write(PCA9685_MODE1, oldmode);
  delay_ms(5);
  PCA9685_write(PCA9685_MODE1, oldmode | 0xa1);
  delay_ms(5);
}

void pca9685_set_mk(int num, int mk) //设置指定通道的脉宽。fd是在pca9685_init时获得的设备描述符，num是通道号（从0开始），mk是脉宽单位是us。周期已经固定为20ms了
{
  u16 ON, OFF;
  ON = 0; //每次周期一开始就输出高电平
  OFF = (u16)((((double)mk) / 20000 * 4096) * 1.0067114);  //最后的1.0067114是校准用的

  PCA9685_write_reg16(LED0_ON_L + 4 * num, ON);
  PCA9685_write_reg16(LED0_OFF_L + 4 * num, OFF);
}


/*******************************************************/
// define static functions 
/******************************************************/
static void PCA9685_write(u8 address, u8 data)
{
  I2C_DRIVER_Write_Bytes(PCA9685_adrr, address, &data, 1);
}

static void PCA9685_write_reg16(u8 address, u16 data)
{
  I2C_DRIVER_Write_Bytes(PCA9685_adrr, address, (u8*)(&data), 2);
}

static void PCA9685_read(char address, u8* rec_buffer, u8 len)
{
  I2C_DRIVER_Read_Bytes(PCA9685_adrr, address, rec_buffer, len);
}