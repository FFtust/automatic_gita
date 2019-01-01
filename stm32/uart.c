#include <stdint.h>
#include <stdio.h>
#include "stm32f10x.h"
#include "uart.h"
#include "GPIO_STM32F10x.h"
#include "mb_communication_protocol.h"

void USART_Configuration(void)
{ 
  GPIO_InitTypeDef GPIO_InitStructure;
  USART_InitTypeDef USART_InitStructure; 

  RCC_APB2PeriphClockCmd(RCC_APB2Periph_USART1,ENABLE);
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA,ENABLE);
            
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_9;          
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP; 
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz; 
  GPIO_Init(GPIOD, &GPIO_InitStructure);           

  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_10;            
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPU;  
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz; 
  GPIO_Init(GPIOD, &GPIO_InitStructure);

  USART_InitStructure.USART_BaudRate = 115200;
  USART_InitStructure.USART_WordLength = USART_WordLength_8b;
  USART_InitStructure.USART_StopBits = USART_StopBits_1;
  USART_InitStructure.USART_Parity = USART_Parity_No;
  USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None;
  USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;
  USART_Init(USART1, &USART_InitStructure); 
  USART_ITConfig(USART1, USART_IT_RXNE, ENABLE);
  USART_Cmd(USART1, ENABLE); 
  USART_ClearITPendingBit(USART1, USART_IT_TC);

}

void USART1_IRQHandler(void)  
{
  uint8_t temp;
	if(USART_GetITStatus(USART1, USART_IT_RXNE) != RESET)
	{   
		temp = USART1->DR;//
		mb_communication_data_push_t(temp);
		USART_ClearITPendingBit(USART1, USART_IT_RXNE);
	}
	if (USART_GetITStatus(USART1, USART_IT_TXE) != RESET) 
	{
		USART_ClearITPendingBit(USART1, USART_IT_TXE);
	}
}

