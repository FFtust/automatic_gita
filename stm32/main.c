#include <stdint.h>
#include <stdio.h>
#include "GPIO_STM32F10x.h"
#include "key.h"
#include "uart.h"
#include "motor.h" 
#include "common.h"
#include "servo.h"
#include "mb_communication_protocol.h"

extern void NVIC_Configuration(void);

void protocol_check(uint8_t *data, uint8_t len)
{
  int i = 0;
  uint8_t servo_id = 0;
  uint8_t servo_angle = 0;
  len = len / 2;
  for(i = 0; i < len; i++)
  {
    servo_id = data[i * 2];
    servo_angle = data[i * 2 + 1];
    set_servo(servo_id, servo_angle);
  }

}


int main()
{
  int32_t i = 0;
  key_init();
  servo_init();
  USART_Configuration();
  NVIC_Configuration();
  mb_communication_init_t();
  mb_communication_register_callback_t(protocol_check);
  // set_servo(0, 42);
  // set_servo(1, 50);
  // set_servo(2, 35);
 while(1)
 {  
   if(is_key_pressed(2))
   {
     set_servo(0, 90);
     set_servo(1, 90);
     set_servo(2, 90);
   }
   else if(is_key_pressed(3))
   {
     set_servo(0, 45);
     set_servo(1, 45);
     set_servo(2, 45);
   }
 }
  return 0;
}