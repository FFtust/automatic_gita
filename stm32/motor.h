#ifndef _MOTOR_H_
#define _MOTOR_H_

void motor_control_init(void);
void motor_control_set_pwm(int motor_id, int pwm);
void motor_forward(int motor_id);
void motor_backward(int motor_id);
void motor_stop(int motor_id);
void all_motor_stop(void);
void motor_control(void);

#endif


// void motor_init_t(void)
// {
//     GPIO_PortClock   (GPIOD, true);
//     GPIO_PinWrite    (GPIOD, 8, 0);
//     GPIO_PinConfigure(GPIOD, 8,
//                       GPIO_OUT_PUSH_PULL, 
//                       GPIO_MODE_OUT2MHZ);
//     GPIO_PinWrite    (GPIOD, 9, 0);
//     GPIO_PinConfigure(GPIOD, 9,
//                       GPIO_OUT_PUSH_PULL, 
//                       GPIO_MODE_OUT2MHZ);
    
//     GPIO_PinWrite    (GPIOD, 10, 0);
//     GPIO_PinConfigure(GPIOD, 10,
//                       GPIO_OUT_PUSH_PULL, 
//                       GPIO_MODE_OUT2MHZ);
//     GPIO_PinWrite    (GPIOD, 11, 0);
//     GPIO_PinConfigure(GPIOD, 11,
//                       GPIO_OUT_PUSH_PULL, 
//                       GPIO_MODE_OUT2MHZ);
// }

// void motor1_run_forward_t()
// {
//   GPIO_PinWrite(GPIOD, 8, 1);
//   GPIO_PinWrite(GPIOD, 9, 0);
// }

// void motor1_run_backward_t()
// {
//   GPIO_PinWrite(GPIOD, 8, 0);
//   GPIO_PinWrite(GPIOD, 9, 1);
// }

// void motor2_run_forward_t()
// {
//   GPIO_PinWrite(GPIOD, 10, 1);
//   GPIO_PinWrite(GPIOD, 11, 0);
// }

// void motor2_run_backward_t()
// {
//   GPIO_PinWrite(GPIOD, 10, 0);
//   GPIO_PinWrite(GPIOD, 11, 1);
// }

// void motor1_stop_t()
// {
//   GPIO_PinWrite(GPIOD, 8, 0);
//   GPIO_PinWrite(GPIOD, 9, 0);
// } 

// void motor2_stop_t()
// {
//   GPIO_PinWrite(GPIOD, 10, 0);
//   GPIO_PinWrite(GPIOD, 11, 0);
// } 

// void motor2_speed(int16_t speed, uint16_t time_ms)
// {
//   uint32_t t = 0;
//   if(speed >= 0)
//   {
//     for(t = 0; t < time_ms; t++)
//     {
//       motor2_run_forward_t();
//       delay_us(speed * 10);
//       motor2_stop_t();
//       delay_us((100 - speed) * 10);
//     }
//   }
//   else
//   {
//     for(t = 0; t < time_ms; t++)
//     {
//       motor2_run_backward_t();
//       delay_us(-speed * 10);
//       motor2_stop_t();
//       delay_us((100 + speed) * 10);
//     }
//   }
// }

  //   if(is_key_pressed(2))
  //   {
  //     motor2_speed(100, 5);
  //     USART_SendData(USART2, 0x01);
  //     for(i = 0; i <= 4 ;i++)
  //     {
  //       motor2_speed(100- 20 * i, 5);
  //     }
  //     motor2_speed(10, 30);
            
            
  //     while(is_key_pressed(2))
  //     {
  //       motor2_stop_t();
  //     }
  //   }
  //   else if(is_key_pressed(3))
  //   {
  //     motor2_speed(-100, 5);

  //     for(i = 0; i <= 4 ;i++)
  //     {
  //       motor2_speed(-100 + 20 * i, 5);
  //     }
  //     motor2_speed(-10, 30);
  //     while(is_key_pressed(3))
  //     {
  //       motor2_stop_t();
  //     }
  //   }
  //   else
  //   {
  //     motor2_stop_t();
  //   }

  //   if(USART1->DR != 0x00)
  //   {
  //      motor2_stop_t();
  //   }
  // }