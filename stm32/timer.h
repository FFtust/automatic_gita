// T1
/*      no remap    partial remap    total remap
  ch1    PA8          PA8             PE9
  ch2    PA9          PA9             PE11
  ch3    PA10         PA10            PE13
  ch4    PA11         PA11            PE14
*/

// T2
/*      no remap(00)    partial remap(01)    partial remap(10)  total remap(11) 
  ch1    PA0              PA15                   PA0               PA15
  ch2    PA1              PB3                    PA1               PB3
  ch3    PA2              PA2                    PB10              PB10
  ch4    PA3              PA3                    PB11              PB11
*/

// T3
/*      no remap    partial remap    total remap
  ch1    PA6          PB4              PC6
  ch2    PA7          PB5              PC7
  ch3    PB0          PB0              PC8
  ch4    PB1          PB1              PC9
*/


// T4
/*      no remap    partial remap
  ch1    PB6          PD12             
  ch2    PB7          PD13        
  ch3    PB8          PD14             
  ch4    PB9          PD15         
*/

#ifndef _TIMER_H_
#define _TIMER_H_

void TIM_Configuration(void);

#endif

