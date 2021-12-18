#ifndef PCA9685_CONTROL_H_
#define PCA9685_CONTROL_H_

void pca9685_init(void);
void pca9685_set_freq(float freq);
void pca9685_set_mk(int num, int mk);

#endif /* PCA9685_CONTROL_H_ */