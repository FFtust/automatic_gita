/**   
 * \par Copyright (C), 2017-2018, MakeBlock
 * \brief   Header for mb_communition.c
 * @file    mb_communition.h
 * @author  fftust
 * @version V1.0.0
 * @date    2018/07/05
 *
 * \par Copyright
 * This software is Copyright (C), 2012-2016, MakeBlock. Use is subject to license \n
 * conditions. The main licensing options available are GPL V2 or Commercial: \n
 *
 * \par Open Source Licensing GPL V2
 * This is the appropriate option if you want to share the source code of your \n
 * application with everyone you distribute it to, and you also want to give them \n
 * the right to share who uses it. If you wish to use this software under Open \n
 * Source Licensing, you must contribute all your source code to the open source \n
 * community in accordance with the GPL Version 2 when your application is \n
 * distributed. See http://www.gnu.org/copyleft/gpl.html
 *
 * \par Description
 * This file is a header for mb_communition.c
 *
 * \par Method List:
 *
 *
 * \par History:
 * <pre>
 * `<Author>`         `<Time>`        `<Version>`        `<Descr>`
 * fftust             2018/07/05      1.0.0              build the new.
 * </pre>
 *
 */

#ifndef _MB_COMMUNICATION_PROTOCOL_H_
#define _MB_COMMUNICATION_PROTOCOL_H_
#include "stdint.h"
#include "mb_communication_package.h"

typedef enum
{
  COMMU_PROTOCOL_GROUP_NONE = 0,
  COMMU_PROTOCOL_GROUP_COMMON,
  COMMU_PROTOCOL_GROUP_NEURONS,
  COMMU_PROTOCOL_GROUP_FF55,
  COMMU_PROTOCOL_GROUP_MAX,
}COMMUNICATION_PROTOCOL_GROUP_ID;

#define COMMON_PROTOCOL_PACKAGE_BUFFER_LEN    (256)
#define COMMON_PROTOCOL_HEAD                  (0xF3)
#define COMMON_PROTOCOL_END                   (0xF4)
#define NEURONS_PROTOCOL_PACKAGE_BUFFER_LEN   (128)
#define NEURONS_PROTOCOL_HEAD                 (0xF0)
#define NEURONS_PROTOCOL_END                  (0xF7)

typedef void (*communication_protocol_cb_t)(uint8_t *data, uint8_t);
typedef int32_t (*communication_protocol_package_put_char_t)(void *package, uint8_t *data, int32_t size);

#define PROTOCOL_CB_PARAMETER_BYTES_MAX   (16)
#define PROTOCOL_FRAME_MAX                (8)
#define QUEUE_BUFFER_RESERVED_BYTES_LEN   (4) 

typedef struct
{
  /* reference @COMMUNICATION_PROTOCOL_GROUP_ID */
  int32_t protocol_tag;
  /* head and end may not be used */
  uint8_t head;
  uint8_t end;
  /* buffer for package */
  communication_package_t *package;
  /* this function capture a package from data stream, 
     the package logic should be defined in this function
  */
  communication_protocol_package_put_char_t protocol_package_put_char;
  /* after received a whole package, this function will be called */
  communication_protocol_cb_t protocol_cb;
  uint8_t cb_para[PROTOCOL_CB_PARAMETER_BYTES_MAX];
}communication_protocol_group_t;

/* for specific protocol */
typedef enum
{
  FSM_COMMON_PROTOCOL_HEADER = 0,
  FSM_COMMON_PROTOCOL_HEADER_CHECK,
  FSM_COMMON_PROTOCOL_LEN_1,
  FSM_COMMON_PROTOCOL_LEN_2,
  FSM_COMMON_PROTOCOL_DATA,
  FSM_COMMON_PROTOCOL_DATA_CHECK,
  FSM_COMMON_PROTOCOL_END,
}commmon_protoco_frame_fsm_state_t;

typedef struct 
{
  commmon_protoco_frame_fsm_state_t fsm_state;
  uint8_t head_check_buffer[4];
  int32_t data_expect_len;
  int32_t data_real_len;
}commmon_protocol_frame_manager_tt;

void mb_communication_init_t(void);
void mb_communication_data_push_t(uint8_t c);
void mb_communication_register_callback_t(communication_protocol_cb_t cb);

#endif /* _MB_COMMUNICATION_PROTOCOL_H_ */

