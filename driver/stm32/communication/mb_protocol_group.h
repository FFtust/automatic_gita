/**   
 * \par Copyright (C), 2017-2018, MakeBlock
 * \brief   Header for protocol_frame_package.c
 * @file    protocol_frame_package.h
 * @author  fftust
 * @version V1.0.0
 * @date    2018/07/04
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
 * Header for protocol_frame_package.c
 *
 * \par Method List:
 *
 *
 * \par History:
 * <pre>
 * `<Author>`         `<Time>`        `<Version>`        `<Descr>`
 * fftust             2018/07/04      1.0.0              build the new.
 * </pre>
 *
 */
#ifndef _PROCOTOL_GROUP_H_
#define _PROCOTOL_GROUP_H_

#include "stdint.h"
#include "mb_err.h"
#include "stdbool.h"

typedef void (* protocol_cb_t)(void *);
typedef int32_t (*protocol_package_put_char_t)(void *protocol, uint8_t *c);

#define PACKAGE_DATA_LEN_MAX (256)
#define PROTOCOL_CB_PARAMETER_BYTES_MAX (16)
#define PROTOCOL_FRAME_MAX (8)

typedef struct
{
  union
  {
    uint8_t data[PACKAGE_DATA_LEN_MAX]; // a cmd package must less than PACKAGE_DATA_LEN_MAX bytes
    struct _neu_info_t
    {
      uint8_t device_id;
      uint8_t service_id;
      uint8_t sub_service_id;  // this id may not exist in some devices
      uint8_t cmd_id;
    }neu_protocol_t;               // for neurons protocol
    struct _common_info_t
    {
      uint8_t head_check;
      uint8_t data_len_high;
      uint8_t data_len_low; 
      uint8_t cmd_id;
    }common_protocol_t;          // for common protocol
  }package_union;
  int32_t protocol_tag;
  uint8_t head;
  uint8_t end;
  uint16_t data_in_index;
  uint16_t channel_tag;
  uint16_t data_in_begin;
  protocol_package_put_char_t protocol_package_put_char;
  protocol_cb_t protocol_cb;
  uint8_t cb_para[PROTOCOL_CB_PARAMETER_BYTES_MAX];
}protocol_group_t;

extern mb_err_t protocol_group_set_default_t(protocol_group_t *protocol);
extern mb_err_t protocol_group_show_t(protocol_group_t *protocol);

extern mb_err_t protocol_package_add_bytes_t(protocol_group_t *protocol, uint8_t *data, uint16_t size);
extern mb_err_t protocol_package_add_checksum_t(protocol_group_t *protocol, uint8_t mark);
extern bool protocol_package_checksum_verify_t(protocol_group_t *protocol, uint8_t check_sum);

extern mb_err_t protocol_package_reset(protocol_group_t *protocol);
extern mb_err_t protocol_package_push_default_t(void *protocol, uint8_t *c);
#endif /* _PROCOTOL_GROUP_H_ */
