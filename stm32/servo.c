#include "pca9685_control.h"
#include "servo.h"

#define SERVO_PULS_COFFICIENT (2000.0 / 180.0)

static int calculate_t_from_angle(int angle);

void servo_init()
{
    pca9685_init();
}

void set_servo(int num, int angle)
{
  pca9685_set_mk(num, calculate_t_from_angle(angle));
}

static int calculate_t_from_angle(int angle)
{
  int ret_t = 500;
  angle = (angle > 180) ? 180 : angle;
  angle = (angle < 0) ? 0 : angle;
 
  ret_t += angle * SERVO_PULS_COFFICIENT; 
  return ret_t;
}