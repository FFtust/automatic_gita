# 自动电子琴
## 写在前面
　　自动电子琴是一个利用业余时间完成的项目，纯属个人爱好。为什么这个项目的名称是
automaic_gita？这是因为最早这个项目是在19年用来实现自动吉他的，因为两个项目都是用
纯舵机控制，因此放在了一起。  
　　自动吉他的完成度较低，故不作详细描述，感兴趣的可观看早期视频：
https://www.bilibili.com/video/BV1jb411k7um?spm_id_from=333.999.0.0

## 成品展示
### 独立演奏设备
![独立设备](https://github.com/FFtust/automatic_gita/blob/master/source/piano/device_shot.jpg)
### 完整设备
![完整设备](https://github.com/FFtust/automatic_gita/blob/master/source/piano/all_shot.jpg)

## 硬件组成
### 硬件框图
![硬件框图](https://github.com/FFtust/automatic_gita/blob/master/source/piano/hardware.png)

### 元器件清单
![硬件框图](https://github.com/FFtust/automatic_gita/blob/master/source/piano/tools_list.jpg)

| 元件 | 数量 | 参数 |备注|
| :-----| :---- | :---- | :---- |
| 5V开关电源 | 1 | 30A | 尽量电流大的 |
| 9g小舵机 | >=61 | 无 | 容易坏，多买几个 |
| stm32F03开发板| 1    | 舵机控制信号 | 具备I2C主控均可 |
| pca9685模块 | >=4 | 16路控制 | 买模块不要芯片|
| usb转串口模块 | 1 |  | |
| 其他 | N| 工具等 |杜邦线、胶枪、螺丝刀...|

## 非权威乐理知识
### 钢琴琴键相关知识
![钢琴琴键](https://github.com/FFtust/automatic_gita/blob/master/source/piano/key.png)  

钢琴上分白键和黑键，7个白键+5个黑键为1组，每个钢琴上都是多个12键组合，每组代表不同的音高。
其中白键是我们熟知的do re mi fa so la xi， 共7个，黑键是这7个音调的扩展，比如位于do re之间的，
就是其中一个黑键代表的音调。do 就是上图中的 C也是上图中的1，找到两个连续的黑键位置，黑键左边的白键就是C（1、do）。
### 乐谱相关知识
![乐谱](https://github.com/FFtust/automatic_gita/blob/master/source/piano/note.png)  

**1=C 4/4  x=82**  
1=C 的意思是，那么乐谱中的1就是钢琴中的do。
如果1 = E，那么乐谱中的1就是钢琴中的mi，2就是钢琴中的fa，以此类推。

**4/4**  
以四分音符为一拍 每小节4拍

**x=82**  
代表的是弹奏速度。
比如写60， 则乐曲的规定速度为每分钟 60 拍,每拍占用的时间是一秒,
半拍是二分之一 秒;当规定速度为每分钟 120 拍时,每拍的时间是半秒,
半拍就是四分之一 秒,依此类推。拍子的基本时值确定之后,音符之间弹奏的时间间隔就确定了。

### 五线谱
看不懂记不住

### MIDI
midi跟我实现的乐谱转舵机控制信号原理上差不多，自己开发也有一番乐趣。
	
## 软件架构
### 信息转化流程图
![信息转化流程图](https://github.com/FFtust/automatic_gita/blob/master/source/piano/sofeware.png)
### 乐谱转化规则
1. 左右手弹奏的乐谱独立编写；
2. 每一个独立的乐谱（如左手乐谱）为一个tuple类型的数据，tuple中包含N个小节的乐谱，也为一个tuple类型，如

``` python
music_table = \
(
	("0", "-", "-", "-"),
	("3", "-", "-", "-", "-", "-", "-", "-", "2", "-", "-", "-", "-", "-", "-", "-"),
	("1", "-", "-", "-", "-", "-", "-", "-", "7-", "-", "-", "-", "-", "-", "-", "-"),
	("6-", "-", "-", "-", "-", "-", "-", "-", "5-", "-", "-", "-", "-", "-", "-", "-"),
	("6", "-", "-", "-", "-", "-", "-", "-", "7-", "-", "-", "-", "-", "-", "-", "-"),
)

music_table_left = \
(
	("0", "-", "-", "-"),
	("1-", "-", "-", "-", "-", "-", "-", "-", "5--", "-", "-", "-", "-", "-", "-", "-"),
	("6--", "-", "-", "-", "-", "-", "-", "-", "3--", "-", "-", "-", "-", "-", "-", "-"),
	("4--", "-", "-", "-", "-", "-", "-", "-", "5--", "-", "-", "-", "-", "-", "-", "-"),
	("4--", "-", "-", "-", "-", "-", "-", "-", "5--", "-", "-", "-", "-", "-", "-", "-"),

)

import sys
sys.path.append('C:\\work\\automatic_gita\\python\\piano')

import music_translate
music_parse = music_translate.music_trans([music_table, music_table_left], beat = 82)
music_parse.music_to_play_table()
music_parse.play_music()
```

3. 描述每一小节的tuple长度可变，根据各小节的最小节拍来定义。如最小节拍为1/4音符，则长度为4，最小节拍为1/16音符，则长度为16.
4. 使用音符<-->舵机对应表来转换成舵机控制信号。

``` python
servo_table = \
{
"1--": 0, "1--#": 1, "2--": 2,"2--#": 3,"3--": 4,"4--": 5, "4--#": 6,"5--": 7,"5--#": 8,"6--": 9,"6--#": 10, "7--": 11,
"1-": 12, "1-#": 13, "2-": 14, "2-#": 15,"3-": 16,"4-": 17, "4-#": 18,"5-": 19,"5-#": 20,"6-": 21,"6-#": 22, "7-": 23,
"1": 24, "1#": 25, "2": 26,"2#": 27,"3": 28,"4": 29, "4#": 30,"5": 31,"5#": 32,"6": 33,"6#": 34, "7": 35,
"1+": 36, "1+#": 37, "2+": 38,"2+#": 39,"3+": 40,"4+": 41, "4+#": 42,"5+": 43,"5+#": 44,"6+": 45,"6+#": 46, "7+": 47,
"1++": 48, "1++#": 49, "2++": 50,"2++#": 51,"3++": 52,"4++": 53, "4++#": 54,"5++": 55,"5++#": 56,"6++": 57,"6++#": 58, "7++": 59,
"1+++":61,
}
```  

5. 存在一个描述每个舵机按下和抬起的角度值，因为舵机安装存在误差，所以角度需要微调。

``` python
SERVO_ID_BASE = 0
NOT_IMPLEMET = 100
FREE_ANGLE = 181

ANG_COM = 50
ANG_BLACK = 40
ANG_OFF_BLACK = 0

servos_angle = \
{
0: [90, ANG_BLACK], 1: [90, ANG_BLACK], 2: [90, 35], 3: [90, 35], 4: [90, 35], 5: [90, 35], 6: [90, ANG_BLACK], 7: [90, 35], 8: [90, ANG_BLACK], 9: [80, 30], 10: [90, ANG_BLACK], 11: [90, 35], 
12: [90, ANG_COM], 13: [90, ANG_BLACK], 14: [80, ANG_COM], 15: [90, ANG_BLACK], 16: [85, ANG_COM], 17: [90, ANG_COM], 18: [90, ANG_BLACK], 19: [90, ANG_COM], 20: [90, ANG_BLACK], 21: [85, ANG_COM], 22: [90, ANG_BLACK], 23: [90, ANG_COM],
24: [90,  ANG_COM], 25: [90, ANG_BLACK], 26: [90, ANG_COM], 27: [90, ANG_BLACK], 28: [90, ANG_COM], 29: [90, ANG_COM], 30: [90, ANG_BLACK], 31: [90, ANG_COM], 32: [90, ANG_BLACK], 33: [90, ANG_COM], 34: [90, ANG_BLACK], 35: [90, ANG_COM], 
36: [90, ANG_COM], 37: [90, ANG_BLACK], 38: [90, ANG_COM], 39: [90, ANG_BLACK], 40: [90, ANG_COM], 41: [90, ANG_COM], 42: [90, ANG_BLACK], 43: [90, ANG_COM], 44: [90, 40], 45: [90, ANG_COM], 46: [90, ANG_BLACK -15], 47: [90, ANG_COM], 
48: [90, ANG_COM], 49: [90, ANG_BLACK], 50: [90, ANG_COM], 51: [90, ANG_BLACK], 52: [90, ANG_COM], 53: [90, ANG_COM], 54: [90, ANG_BLACK], 55: [90, ANG_COM], 56: [90, ANG_BLACK], 57: [90, ANG_COM], 58: [90, ANG_BLACK], 59: [90, ANG_COM], 
60: [90, ANG_COM], 61: [90, ANG_BLACK], 62: [90, ANG_COM], 63: [90, ANG_BLACK], 64: [90, ANG_COM], 
100: [90, 90]
}
```

### 代码构成
**代码目录说明**
*aumatic_gita*  
　*driver*  
　　*stm32*  
　*music*  
　　*python*  
　　　*gita*  
　　　*pinao*  
　*source*  
　　*pinao*  

其中
*driver*  
该目录下是一个STM32的工程，用来编写驱动PCA9685的程序，即舵机控制程序，
其输出是第N个舵机转动到M角度，输入是串口指令。
*music*
该目录下是用python编写的程序，主要用来将乐谱信息转化成舵机控制信号，然后通过USB串口发送到下位机。  
_gita_ 是早期实现的自动jita程序，完成度较低。
_pinao_ 是近期实现的自动电子琴程序，完成度较高。  


## 视频案例
本项目完成的主要视频上传在B站，欢迎观看。
克罗地亚狂想曲（piano）:  
https://www.bilibili.com/video/BV1Zq4y1T7Gv?spm_id_from=333.999.0.0  
野蜂飞舞（piano）:  
https://www.bilibili.com/video/BV1wQ4y1k7Sx?spm_id_from=333.999.0.0  
天空之城（gita）:  
https://www.bilibili.com/video/BV1jb411k7um?spm_id_from=333.999.0.0  

