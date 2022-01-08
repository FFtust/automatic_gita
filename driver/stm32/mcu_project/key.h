#ifndef _KEY_H_
#define _KEY_H_

#include <stdint.h>
#include <stdio.h>

#define KEY_S0_IO         (6)
#define KEY_S1_IO         (7)
#define KEY_S2_IO         (8)
#define KEY_S3_IO         (9)

#define KEY_GPIO_GROUP    (GPIOC)



extern void key_init(void);
extern uint8_t is_key_pressed(uint8_t key_id);
extern int wait_until_key_releaseded(uint8_t key_id);

#endif