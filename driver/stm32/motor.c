#include <stdint.h>
#include <stdio.h>
#include "GPIO_STM32F10x.h"
#include "motor.h"
#include "common.h"

typedef struct
{
  GPIO_TypeDef *io1_group;
  int io1_num;
  GPIO_TypeDef *io2_group;
  int io2_num;
  int pwm;
  uint8_t io1_level;
  uint8_t io2_level;
	int count;
	int run_time;
}motor_structure_t;

#define MOTOR_NUM       (6)
motor_structure_t motor[MOTOR_NUM] = \
{
  /* 0 */ {GPIOA, 4, GPIOA, 5, 0},
  /* 1 */ {GPIOA, 6, GPIOA, 7, 0},
  /* 2 */ {GPIOC, 4, GPIOC, 5, 0},
  /* 3 */ {GPIOB, 0, GPIOB, 1, 0},
  /* 4 */ {GPIOD, 14, GPIOD, 15, 0},
  /* 5 */ {GPIOE, 8, GPIOE, 9, 0},
  // /* 6 */ {GPIOE, 10, GPIOE, 11, 0},
  // /* 7 */ {GPIOE, 12, GPIOE, 13, 0},
  // /* 8 */ {GPIOE, 14, GPIOE, 15, 0},
  // /* 9 */ {GPIOB, 12, GPIOB, 13, 0},
  // /* 10 */ {GPIOB, 14, GPIOB, 15, 0},
  // /* 11 */ {GPIOD, 8, GPIOD, 9, 0},
  // /* 12 */ {GPIOD, 10, GPIOD, 11, 0},
  // /* 13 */ {GPIOD, 12, GPIOD, 13, 0},
//  /* 14 */ {GPIOD, 14, GPIOD, 15, 0},
};
	
	
void motor_control_init(void)
{
	int i = 0;

  for(; i < MOTOR_NUM; i++)
	{
	  if(motor[i].io1_group != NULL)
		{
		  GPIO_PortClock   (motor[i].io1_group, true);
      GPIO_PinWrite    (motor[i].io1_group, motor[i].io1_num, 0);
      GPIO_PinConfigure(motor[i].io1_group, motor[i].io1_num,
                        GPIO_OUT_PUSH_PULL, 
                        GPIO_MODE_OUT2MHZ);
		}
		if(motor[i].io2_group != NULL)
		{
		  GPIO_PortClock   (motor[i].io2_group, true);
      GPIO_PinWrite    (motor[i].io2_group, motor[i].io2_num, 0);
      GPIO_PinConfigure(motor[i].io2_group, motor[i].io2_num,
                        GPIO_OUT_PUSH_PULL, 
                        GPIO_MODE_OUT2MHZ);		
		}
    motor[i].io1_level = 0;
    motor[i].io2_level = 0;
     
    motor[i].pwm = 0;
    motor[i].count = 0;
    motor[i].run_time = 0;
	}
}

void motor_control_set_pwm(int motor_id, int pwm)
{
  motor[motor_id].pwm = pwm;
  motor[motor_id].count = 0;
}

void motor_forward(int motor_id)
{
  GPIO_PinWrite(motor[motor_id].io1_group, motor[motor_id].io1_num, 1);
  GPIO_PinWrite(motor[motor_id].io2_group, motor[motor_id].io2_num, 0);
}

void motor_backward(int motor_id)
{
  GPIO_PinWrite(motor[motor_id].io1_group, motor[motor_id].io1_num, 0);
  GPIO_PinWrite(motor[motor_id].io2_group, motor[motor_id].io2_num, 1);
}

void motor_stop(int motor_id)
{
  GPIO_PinWrite(motor[motor_id].io1_group, motor[motor_id].io1_num, 0);
  GPIO_PinWrite(motor[motor_id].io2_group, motor[motor_id].io2_num, 0);
}

void all_motor_stop(void)
{
	int i = 0;
  for(; i < MOTOR_NUM; i++)
	{
	  motor_control_set_pwm(i, 0);
	}
}

/* 0 - 5 */
void sweep_motor_control(int motor_id)
{
  if(motor[motor_id].pwm >= -5 && motor[motor_id].pwm <= 5)
  {
    motor_stop(motor_id);
		motor[motor_id].count++;
		return;
  }

  if(motor[motor_id].pwm >= 0)
  {
    if(motor[motor_id].count % 100 < motor[motor_id].pwm)
    {
      motor_forward(motor_id);
      motor[motor_id].io1_level = 1;
      motor[motor_id].io2_level = 0;
    }
    else
    {
      motor_stop(motor_id);
      motor[motor_id].io1_level = 0;
      motor[motor_id].io2_level = 0;
    }
  }
  else
  {
    if(motor[motor_id].count % 100 < -motor[motor_id].pwm)
    {
      motor_backward(motor_id);
      motor[motor_id].io1_level = 0;
      motor[motor_id].io2_level = 1;
    }
    else
    {
      motor_stop(motor_id);
      motor[motor_id].io1_level = 0;
      motor[motor_id].io2_level = 0;
    }
  }
  motor[motor_id].count++;
}

void motor_control()
{
  int8_t i = 0;

  for(i = 0; i < MOTOR_NUM; i++)
  {
    sweep_motor_control(i);
  }
}
