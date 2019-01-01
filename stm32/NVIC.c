#include <stdint.h>
#include <stdio.h>
#include "GPIO_STM32F10x.h"
#include "NVIC.h"

void NVIC_Configuration(void)
{
  NVIC_InitTypeDef NVIC_InitStructure;
    
  /* Set the Vector Table base location at 0x08000000 */
  NVIC_SetVectorTable(NVIC_VectTab_FLASH, 0x0);   
  NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);
  
  // NVIC_InitStructure.NVIC_IRQChannel = TIM3_IRQn;
  // NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 1;
  // NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;
  // NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
  // NVIC_Init(&NVIC_InitStructure);

  NVIC_InitStructure.NVIC_IRQChannel = USART1_IRQn;     
  NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 3;
  NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;  
  NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
  NVIC_Init(&NVIC_InitStructure); 
    
}
