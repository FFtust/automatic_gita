#include <stdint.h>
#include <stdio.h>
#include "GPIO_STM32F10x.h"
#include "timer.h"

extern void sweep_motor_control(int motor_id);

__IO uint16_t CCR1_Val = 100;
__IO uint16_t CCR2_Val = 100;
__IO uint16_t CCR3_Val = 100;
__IO uint16_t CCR4_Val = 100;

void TIM3_Configuration(void)
{
  TIM_TimeBaseInitTypeDef  TIM_TimeBaseStructure;
  TIM_OCInitTypeDef  TIM_OCInitStructure;
  uint16_t PrescalerValue = 0;
                               
  PrescalerValue = (uint16_t)720 - 1;;
  RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM3, ENABLE);
  /* Time base configuration */
  TIM_TimeBaseStructure.TIM_Period = 10;
  TIM_TimeBaseStructure.TIM_Prescaler = 0;
  TIM_TimeBaseStructure.TIM_ClockDivision = 0;
 
  TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;
  TIM_TimeBaseInit(TIM3, &TIM_TimeBaseStructure);
  /* Prescaler configuration */
  TIM_PrescalerConfig(TIM3, PrescalerValue, TIM_PSCReloadMode_Immediate);

  /* Output Compare Timing Mode configuration: Channel1 */
  TIM_OCInitStructure.TIM_OCMode = TIM_OCMode_Timing;
  TIM_OCInitStructure.TIM_OutputState = TIM_OutputState_Enable;
  TIM_OCInitStructure.TIM_Pulse = CCR1_Val;
  TIM_OCInitStructure.TIM_OCPolarity = TIM_OCPolarity_High;
  
  TIM_OC1Init(TIM3, &TIM_OCInitStructure);
  
  TIM_OC1PreloadConfig(TIM3, TIM_OCPreload_Disable);

  TIM_ITConfig(TIM3, TIM_IT_Update, ENABLE);
  // TIM_ITConfig(TIM3, TIM_IT_CC1, ENABLE);//  | TIM_IT_CC2 | TIM_IT_CC3 | TIM_IT_CC4, ENABLE);
  /* TIM3 enable counter */
  TIM_Cmd(TIM3, ENABLE);
}

void TIM_Configuration(void)
{
  TIM3_Configuration();
}

void TIM3_IRQHandler(void)
{
	 int i = 0;
  if (TIM_GetITStatus(TIM3, TIM_IT_Update) != RESET)
  {
    TIM_ClearITPendingBit(TIM3, TIM_IT_Update);
		for(i = 0; i < 6; i++)
		{
      sweep_motor_control(i);
		}
  }
  
}


void TIM1_Configuration(void)
{
  TIM_TimeBaseInitTypeDef  TIM_TimeBaseStructure;
  TIM_OCInitTypeDef        TIM_OCInitStructure;
  uint16_t PrescalerValue = 0;
                               
  PrescalerValue = (uint16_t)720 - 1;;
  RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM3, ENABLE);
  /* Time base configuration */
  TIM_TimeBaseStructure.TIM_Period = 10;
  TIM_TimeBaseStructure.TIM_Prescaler = 0;
  TIM_TimeBaseStructure.TIM_ClockDivision = 0;
 
  TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;
  TIM_TimeBaseInit(TIM1, &TIM_TimeBaseStructure);
  /* Prescaler configuration */
  TIM_PrescalerConfig(TIM1, PrescalerValue, TIM_PSCReloadMode_Immediate);

  TIM_OC1Init(TIM1, &TIM_OCInitStructure);
  
  TIM_OC1PreloadConfig(TIM1, TIM_OCPreload_Disable);

  TIM_ITConfig(TIM1, TIM_IT_Update, ENABLE);
  // TIM_ITConfig(TIM1, TIM_IT_CC1, ENABLE);//  | TIM_IT_CC2 | TIM_IT_CC3 | TIM_IT_CC4, ENABLE);
  /* TIM1 enable counter */
  TIM_Cmd(TIM1, ENABLE);
}

void TIM2_PWM_Init(u16 arr, u16 psc)
{
  GPIO_InitTypeDef          GPIO_InitStrue;
  TIM_OCInitTypeDef         TIM_OCInitStrue;
  TIM_TimeBaseInitTypeDef   TIM_TimeBaseInitStrue;
  
  RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM2,ENABLE);        
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_AFIO,ENABLE);
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA,ENABLE);
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB,ENABLE);

  GPIO_InitStrue.GPIO_Pin = GPIO_Pin_15;         
  GPIO_InitStrue.GPIO_Mode = GPIO_Mode_AF_PP;    
  GPIO_InitStrue.GPIO_Speed = GPIO_Speed_50MHz; 
  GPIO_Init(GPIOA, &GPIO_InitStrue);         

  GPIO_InitStrue.GPIO_Pin = GPIO_Pin_3;         
  GPIO_InitStrue.GPIO_Mode = GPIO_Mode_AF_PP;   
  GPIO_InitStrue.GPIO_Speed = GPIO_Speed_50MHz; 
  GPIO_Init(GPIOB, &GPIO_InitStrue);            
  
  GPIO_InitStrue.GPIO_Pin = GPIO_Pin_2;         
  GPIO_InitStrue.GPIO_Mode = GPIO_Mode_AF_PP;   
  GPIO_InitStrue.GPIO_Speed = GPIO_Speed_50MHz; 
  GPIO_Init(GPIOA, &GPIO_InitStrue);            

  GPIO_InitStrue.GPIO_Pin = GPIO_Pin_3;        
  GPIO_InitStrue.GPIO_Mode = GPIO_Mode_AF_PP;   
  GPIO_InitStrue.GPIO_Speed = GPIO_Speed_50MHz; 
  GPIO_Init(GPIOA, &GPIO_InitStrue);            
  
  GPIO_PinRemapConfig(GPIO_PartialRemap1_TIM2, ENABLE);

  TIM_TimeBaseInitStrue.TIM_Period = arr;   
  TIM_TimeBaseInitStrue.TIM_Prescaler = psc;       
  TIM_TimeBaseInitStrue.TIM_CounterMode = TIM_CounterMode_Up;
  TIM_TimeBaseInitStrue.TIM_ClockDivision = TIM_CKD_DIV1; 
  TIM_TimeBaseInit(TIM2, &TIM_TimeBaseInitStrue); 
  
  TIM_OCInitStrue.TIM_OCMode = TIM_OCMode_PWM2; 
  TIM_OCInitStrue.TIM_OCPolarity = TIM_OCPolarity_High;
  TIM_OCInitStrue.TIM_OutputState = TIM_OutputState_Enable;
  TIM_OC1Init(TIM2, &TIM_OCInitStrue); 

  TIM_OCInitStrue.TIM_OCMode = TIM_OCMode_PWM2;
  TIM_OCInitStrue.TIM_OCPolarity = TIM_OCPolarity_High;
  TIM_OCInitStrue.TIM_OutputState = TIM_OutputState_Enable;
  TIM_OC2Init(TIM2, &TIM_OCInitStrue);

  TIM_OCInitStrue.TIM_OCMode = TIM_OCMode_PWM2;
  TIM_OCInitStrue.TIM_OCPolarity = TIM_OCPolarity_High;
  TIM_OCInitStrue.TIM_OutputState = TIM_OutputState_Enable;
  TIM_OC3Init(TIM2, &TIM_OCInitStrue);

  TIM_OCInitStrue.TIM_OCMode = TIM_OCMode_PWM2;
  TIM_OCInitStrue.TIM_OCPolarity = TIM_OCPolarity_High;
  TIM_OCInitStrue.TIM_OutputState = TIM_OutputState_Enable;
  TIM_OC4Init(TIM2, &TIM_OCInitStrue);

  TIM_OC2PreloadConfig(TIM2, TIM_OCPreload_Enable);
  TIM_Cmd(TIM2, ENABLE);   
}


void TIM3_PWM_Init(u16 arr, u16 psc)
{
  GPIO_InitTypeDef          GPIO_InitStrue;
  TIM_OCInitTypeDef         TIM_OCInitStrue;
  TIM_TimeBaseInitTypeDef   TIM_TimeBaseInitStrue;
  
  RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM3,ENABLE);        //使能TIM3和相关GPIO时钟
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_AFIO,ENABLE);   // 使能GPIOB时钟(LED在BP5引脚),使能AFIO时钟(定时器3通道2需要重映射到BP5引脚)
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB,ENABLE);
  

  GPIO_InitStrue.GPIO_Pin = GPIO_Pin_4;           // TIM_CH2
  GPIO_InitStrue.GPIO_Mode = GPIO_Mode_AF_PP;     // 复用推挽
  GPIO_InitStrue.GPIO_Speed = GPIO_Speed_50MHz;   //设置最大输出速度
  GPIO_Init(GPIOB, &GPIO_InitStrue);              //GPIO端口初始化设置

  GPIO_InitStrue.GPIO_Pin = GPIO_Pin_5;           // TIM_CH2
  GPIO_InitStrue.GPIO_Mode = GPIO_Mode_AF_PP;     // 复用推挽
  GPIO_InitStrue.GPIO_Speed = GPIO_Speed_50MHz;   //设置最大输出速度
  GPIO_Init(GPIOB, &GPIO_InitStrue);              //GPIO端口初始化设置
  
  GPIO_InitStrue.GPIO_Pin = GPIO_Pin_0;           // TIM_CH2
  GPIO_InitStrue.GPIO_Mode = GPIO_Mode_AF_PP;     // 复用推挽
  GPIO_InitStrue.GPIO_Speed = GPIO_Speed_50MHz;   //设置最大输出速度
  GPIO_Init(GPIOB, &GPIO_InitStrue);              //GPIO端口初始化设置

  GPIO_InitStrue.GPIO_Pin = GPIO_Pin_1;           // TIM_CH2
  GPIO_InitStrue.GPIO_Mode = GPIO_Mode_AF_PP;     // 复用推挽
  GPIO_InitStrue.GPIO_Speed = GPIO_Speed_50MHz;   //设置最大输出速度
  GPIO_Init(GPIOB, &GPIO_InitStrue);              //GPIO端口初始化设置

  GPIO_PinRemapConfig(GPIO_PartialRemap_TIM3, ENABLE);
  
  TIM_TimeBaseInitStrue.TIM_Period = arr;    //设置自动重装载值
  TIM_TimeBaseInitStrue.TIM_Prescaler = psc;        //预分频系数
  TIM_TimeBaseInitStrue.TIM_CounterMode = TIM_CounterMode_Up;    //计数器向上溢出
  TIM_TimeBaseInitStrue.TIM_ClockDivision = TIM_CKD_DIV1;        //时钟的分频因子，起到了一点点的延时作用，一般设为TIM_CKD_DIV1
  TIM_TimeBaseInit(TIM3, &TIM_TimeBaseInitStrue);        //TIM3初始化设置(设置PWM的周期)
  
  TIM_OCInitStrue.TIM_OCMode = TIM_OCMode_PWM2;        // PWM模式2:CNT>CCR时输出有效
  TIM_OCInitStrue.TIM_OCPolarity = TIM_OCPolarity_High;// 设置极性-有效为高电平
  TIM_OCInitStrue.TIM_OutputState = TIM_OutputState_Enable;// 输出使能
  TIM_OC1Init(TIM3, &TIM_OCInitStrue);        //TIM3的通道2PWM 模式设置

  TIM_OCInitStrue.TIM_OCMode = TIM_OCMode_PWM2;        // PWM模式2:CNT>CCR时输出有效
  TIM_OCInitStrue.TIM_OCPolarity = TIM_OCPolarity_High;// 设置极性-有效为高电平
  TIM_OCInitStrue.TIM_OutputState = TIM_OutputState_Enable;// 输出使能
  TIM_OC2Init(TIM3, &TIM_OCInitStrue);        //TIM3的通道2PWM 模式设置

  TIM_OCInitStrue.TIM_OCMode = TIM_OCMode_PWM2;        // PWM模式2:CNT>CCR时输出有效
  TIM_OCInitStrue.TIM_OCPolarity = TIM_OCPolarity_High;// 设置极性-有效为高电平
  TIM_OCInitStrue.TIM_OutputState = TIM_OutputState_Enable;// 输出使能
  TIM_OC3Init(TIM3, &TIM_OCInitStrue);        //TIM3的通道2PWM 模式设置

  TIM_OCInitStrue.TIM_OCMode = TIM_OCMode_PWM2;        // PWM模式2:CNT>CCR时输出有效
  TIM_OCInitStrue.TIM_OCPolarity = TIM_OCPolarity_High;// 设置极性-有效为高电平
  TIM_OCInitStrue.TIM_OutputState = TIM_OutputState_Enable;// 输出使能
  TIM_OC4Init(TIM3, &TIM_OCInitStrue);        //TIM3的通道2PWM 模式设置

  TIM_OC2PreloadConfig(TIM3, TIM_OCPreload_Enable);        //使能预装载寄存器
  
  TIM_Cmd(TIM3,ENABLE);        //使能TIM3
}

void TIM4_PWM_Init(u16 arr, u16 psc)
{
  GPIO_InitTypeDef          GPIO_InitStrue;
  TIM_OCInitTypeDef         TIM_OCInitStrue;
  TIM_TimeBaseInitTypeDef   TIM_TimeBaseInitStrue;
  
  RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM2,ENABLE);        
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_AFIO,ENABLE);
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB,ENABLE);
  

  GPIO_InitStrue.GPIO_Pin = GPIO_Pin_6;         
  GPIO_InitStrue.GPIO_Mode = GPIO_Mode_AF_PP;    
  GPIO_InitStrue.GPIO_Speed = GPIO_Speed_50MHz; 
  GPIO_Init(GPIOB, &GPIO_InitStrue);         

  GPIO_InitStrue.GPIO_Pin = GPIO_Pin_7;         
  GPIO_InitStrue.GPIO_Mode = GPIO_Mode_AF_PP;   
  GPIO_InitStrue.GPIO_Speed = GPIO_Speed_50MHz; 
  GPIO_Init(GPIOB, &GPIO_InitStrue);            
  
  GPIO_InitStrue.GPIO_Pin = GPIO_Pin_8;         
  GPIO_InitStrue.GPIO_Mode = GPIO_Mode_AF_PP;   
  GPIO_InitStrue.GPIO_Speed = GPIO_Speed_50MHz; 
  GPIO_Init(GPIOB, &GPIO_InitStrue);            

  GPIO_InitStrue.GPIO_Pin = GPIO_Pin_9;        
  GPIO_InitStrue.GPIO_Mode = GPIO_Mode_AF_PP;   
  GPIO_InitStrue.GPIO_Speed = GPIO_Speed_50MHz; 
  GPIO_Init(GPIOB, &GPIO_InitStrue);            
  
  TIM_TimeBaseInitStrue.TIM_Period = arr;   
  TIM_TimeBaseInitStrue.TIM_Prescaler = psc;       
  TIM_TimeBaseInitStrue.TIM_CounterMode = TIM_CounterMode_Up;
  TIM_TimeBaseInitStrue.TIM_ClockDivision = TIM_CKD_DIV1; 
  TIM_TimeBaseInit(TIM4, &TIM_TimeBaseInitStrue); 
  
  TIM_OCInitStrue.TIM_OCMode = TIM_OCMode_PWM2; 
  TIM_OCInitStrue.TIM_OCPolarity = TIM_OCPolarity_High;
  TIM_OCInitStrue.TIM_OutputState = TIM_OutputState_Enable;
  TIM_OC1Init(TIM4, &TIM_OCInitStrue); 

  TIM_OCInitStrue.TIM_OCMode = TIM_OCMode_PWM2;
  TIM_OCInitStrue.TIM_OCPolarity = TIM_OCPolarity_High;
  TIM_OCInitStrue.TIM_OutputState = TIM_OutputState_Enable;
  TIM_OC2Init(TIM4, &TIM_OCInitStrue);

  TIM_OCInitStrue.TIM_OCMode = TIM_OCMode_PWM2;
  TIM_OCInitStrue.TIM_OCPolarity = TIM_OCPolarity_High;
  TIM_OCInitStrue.TIM_OutputState = TIM_OutputState_Enable;
  TIM_OC3Init(TIM4, &TIM_OCInitStrue);

  TIM_OCInitStrue.TIM_OCMode = TIM_OCMode_PWM2;
  TIM_OCInitStrue.TIM_OCPolarity = TIM_OCPolarity_High;
  TIM_OCInitStrue.TIM_OutputState = TIM_OutputState_Enable;
  TIM_OC4Init(TIM4, &TIM_OCInitStrue);

  TIM_OC2PreloadConfig(TIM4, TIM_OCPreload_Enable);
  TIM_Cmd(TIM4, ENABLE);   
}

// TIM_SetCompare2(TIM3,led0pwmval);