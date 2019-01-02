#include <stdint.h>
#include <stdio.h>
#include "GPIO_STM32F10x.h"
#include "key.h"
#include "uart.h"
#include "motor.h" 
#include "common.h"
#include "pca9685_control.h"
#include "mb_communication_protocol.h"

extern void NVIC_Configuration(void);

void protocol_check(uint8_t *data, uint8_t len)
{
  uint8_t motor_id = 0;
  int8_t motor_power = 0;
  motor_id = data[0];
  motor_power = data[1];
  motor_control_set_pwm(motor_id, motor_power);
}


int main()
{
  int32_t i = 0;
  // motor_control_init();
  key_init();
  pca9685_init();
  // USART_Configuration();
  // TIM_Configuration();
  NVIC_Configuration();
  // mb_communication_init_t();
  // mb_communication_register_callback_t(protocol_check);
 while(1)
 {
//   if(is_key_pressed(2))
   {
     pca9685_set_mk(0, 500);
   }
//   else if(is_key_pressed(1))
	 delay_ms(1000);
   {
     pca9685_set_mk(0, 1500);
   }
	 delay_ms(1000);
 }
  return 0;
}