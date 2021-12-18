#include <stdint.h>
#include <stdio.h>
#include "GPIO_STM32F10x.h"
#include "key.h"

uint8_t key_io_map[4] = {KEY_S0_IO, KEY_S1_IO, KEY_S2_IO, KEY_S3_IO};

void key_init(void)
{
	  GPIO_PortClock   (KEY_GPIO_GROUP, true);
    GPIO_PinConfigure(GPIOD, KEY_S0_IO,
                      GPIO_IN_PULL_UP, 
                      GPIO_MODE_OUT2MHZ);
	
    GPIO_PinConfigure(GPIOD, KEY_S1_IO,
                      GPIO_IN_PULL_UP, 
                      GPIO_MODE_OUT2MHZ);
	
    GPIO_PinConfigure(GPIOD, KEY_S2_IO,
                      GPIO_IN_PULL_UP, 
                      GPIO_MODE_OUT2MHZ);
	
    GPIO_PinConfigure(GPIOD, KEY_S3_IO,
                      GPIO_IN_PULL_UP, 
                      GPIO_MODE_OUT2MHZ);
}

uint8_t is_key_pressed(uint8_t key_id)
{
	if(GPIO_PinRead (KEY_GPIO_GROUP, key_io_map[key_id]))
	{
	  return 0;
	}
	else
	{
	  return 1;
	}
}

int wait_until_key_releaseded(uint8_t key_id)
{
	while(is_key_pressed(key_id))
	{
	  ;
	}
   return 0;
}