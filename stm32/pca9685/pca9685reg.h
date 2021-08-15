#ifndef PCA9685REG_H_
#define PCA9685REG_H_

#define PCA9685_adrr 0x80 // 1+A5+A4+A3+A2+A1+A0+w/r
#define PCA9685_adrr2 0x82 // 1+A5+A4+A3+A2+A1+A0+w/r
#define PCA9685_adrr3 0x84 // 1+A5+A4+A3+A2+A1+A0+w/r
#define PCA9685_adrr4 0x86 // 1+A5+A4+A3+A2+A1+A0+w/r

#define PCA9685_SUBADR1 0x02
#define PCA9685_SUBADR2 0x03
#define PCA9685_SUBADR3 0x04
#define PCA9685_MODE1 0x00
#define PCA9685_PRESCALE 0xFE
#define LED0_ON_L 0x06
#define LED0_ON_H 0x07
#define LED0_OFF_L 0x08
#define LED0_OFF_H 0x09
#define ALLLED_ON_L 0xFA
#define ALLLED_ON_H 0xFB
#define ALLLED_OFF_L 0xFC
#define ALLLED_OFF_H 0xFD

#endif /* PCA9685REG_H_ */