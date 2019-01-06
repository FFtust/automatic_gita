/**   
 * \par Copyright (C), 2017-2018, MakeBlock
 * \brief   Driver for makeblock communication protocol
 * @file    mb_communition_protocol.c
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
 * This file is a drive for communition protocol .
 *
 * \par Method List:
 *
 *
 * \par History:
 * <pre>
 * `<Author>`         `<Time>`        `<Version>`        `<Descr>`
 * fftust             2018/07/4        1.0.0              build the new.
 * </pre>
 *
 */

#include <stdint.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#include "mb_communication_protocol.h"

static int32_t mb_communication_common_protocol_package_push_chars_t(void *protocol_in, uint8_t *data, int32_t size);
static int32_t mb_communication_ff55_protocol_package_push_chars_t(void *protocol_in, uint8_t *data, int32_t size);

static void mb_communication_protocol_set_default_t(communication_protocol_group_t *protocol);
void mb_communication_protocol_create_t(int32_t protocol_group_id, communication_protocol_group_t **protocol_out);

static communication_protocol_group_t *communication_protocol_group;

void mb_communication_data_push_t(uint8_t c)
{
  mb_communication_ff55_protocol_package_push_chars_t(communication_protocol_group, &c, 1);
}
void mb_communication_init_t(void)
{
  mb_communication_protocol_create_t(COMMU_PROTOCOL_GROUP_FF55, &communication_protocol_group);
}

void mb_communication_register_callback_t(communication_protocol_cb_t cb)
{
  communication_protocol_group->protocol_cb = cb;
}

void mb_communication_protocol_create_t(int32_t protocol_group_id, communication_protocol_group_t **protocol_out)
{  
  communication_package_t *package = NULL;
  communication_protocol_group_t *common_protocol = NULL;
    
  if(protocol_group_id == COMMU_PROTOCOL_GROUP_COMMON)
  {
    common_protocol = (communication_protocol_group_t *)malloc(sizeof(communication_protocol_group_t));
    memset(common_protocol, 0, sizeof(communication_protocol_group_t));
    if(common_protocol ==  NULL)
    {
      (*protocol_out) = NULL;
      return;
    }
    mb_communication_package_create_t(COMMON_PROTOCOL_PACKAGE_BUFFER_LEN, &package);
    common_protocol->package = package;
    mb_communication_protocol_set_default_t(common_protocol);
    common_protocol->protocol_tag = COMMU_PROTOCOL_GROUP_COMMON;
    common_protocol->head = COMMON_PROTOCOL_HEAD;
    common_protocol->end = COMMON_PROTOCOL_END;
    // common_protocol->protocol_cb = mb_communication_callback_t;
    common_protocol->protocol_package_put_char = mb_communication_common_protocol_package_push_chars_t;
    (*protocol_out) = common_protocol;
  }
  else if(protocol_group_id == COMMU_PROTOCOL_GROUP_FF55)
  {
    common_protocol = (communication_protocol_group_t *)malloc(sizeof(communication_protocol_group_t));
    memset(common_protocol, 0, sizeof(communication_protocol_group_t));
    if(common_protocol ==  NULL)
    {
      (*protocol_out) = NULL;
      return;
    }
    mb_communication_package_create_t(COMMON_PROTOCOL_PACKAGE_BUFFER_LEN, &package);
    common_protocol->package = package;
    mb_communication_protocol_set_default_t(common_protocol);
    common_protocol->protocol_tag = COMMU_PROTOCOL_GROUP_FF55;
    common_protocol->head = 0x00;
    common_protocol->end = 0x00;

    (*protocol_out) = common_protocol;
  }
}

void mb_communication_protocol_cleanup_t(communication_protocol_group_t *protocol)
{
  if(protocol == NULL)
  {
    return;
  }
  free(protocol->package->data);
  free(protocol->package);
  free(protocol);
}

static int32_t mb_communication_common_protocol_package_push_chars_t(void *protocol_in, uint8_t *data, int32_t size)
{
  static commmon_protocol_frame_manager_tt frame_manager; //  = {.fsm_state = FSM_COMMON_PROTOCOL_HEADER};
  int32_t ret = 0;
  uint8_t c = 0;
  int32_t i = 0;
    
  communication_protocol_group_t *protocol = (communication_protocol_group_t *)(protocol_in);

  for(i = 0; i < size; i++)
  {
    c = data[i];
    switch(frame_manager.fsm_state)
    {
      case FSM_COMMON_PROTOCOL_HEADER:
      /* head byte will not be pushed */
      if(protocol->head == c)
      {
        frame_manager.head_check_buffer[0] = c;
        protocol->package->data_in_index = 0;
        frame_manager.data_expect_len = 0;
        frame_manager.data_real_len = 0;
        frame_manager.fsm_state = FSM_COMMON_PROTOCOL_HEADER_CHECK;
      }
      else
      {
        ret = -1;
      }
      break;

      case FSM_COMMON_PROTOCOL_HEADER_CHECK:
        frame_manager.head_check_buffer[1] = c;
        frame_manager.fsm_state = FSM_COMMON_PROTOCOL_LEN_1;
      break;

      case FSM_COMMON_PROTOCOL_LEN_1:
        frame_manager.head_check_buffer[2] = c;
        frame_manager.fsm_state = FSM_COMMON_PROTOCOL_LEN_2;
      break;

      case FSM_COMMON_PROTOCOL_LEN_2:
        frame_manager.head_check_buffer[3] = c;
        
        if(frame_manager.head_check_buffer[1] == ((frame_manager.head_check_buffer[0] + frame_manager.head_check_buffer[2] + frame_manager.head_check_buffer[3]) & 0xFF))
        {
          frame_manager.data_expect_len = frame_manager.head_check_buffer[2] + frame_manager.head_check_buffer[3] * 256;
          frame_manager.fsm_state = FSM_COMMON_PROTOCOL_DATA;
        }
        else
        {
          frame_manager.fsm_state = FSM_COMMON_PROTOCOL_HEADER;
          ret = -1;
        }
      break;

      case FSM_COMMON_PROTOCOL_DATA:
        mb_communication_package_add_bytes_t(protocol->package, &c, 1);
        frame_manager.data_real_len++;

        if(frame_manager.data_expect_len == frame_manager.data_real_len)
        {
          frame_manager.fsm_state = FSM_COMMON_PROTOCOL_DATA_CHECK;
        }
      break;

      case FSM_COMMON_PROTOCOL_DATA_CHECK:
        {
          uint8_t sum = 0;
          sum = mb_communication_package_calculate_checksum_t(protocol->package, 0, 0xFF);
          if(sum == c)
          {
            frame_manager.fsm_state = FSM_COMMON_PROTOCOL_END;
          }
          else
          {
            frame_manager.fsm_state = FSM_COMMON_PROTOCOL_HEADER;
            ret = -1;
          }
        }
        break;

      case FSM_COMMON_PROTOCOL_END:
        if(protocol->end == c)
        {
          uint8_t buffer[64];
          memcpy(buffer, protocol->package->data + 1, frame_manager.data_real_len);
          buffer[frame_manager.data_real_len] = '\0';
          if(protocol->protocol_cb)
          {
            // protocol->protocol_cb((uint8_t *)buffer, protocol->package->data + 1); /* execute the call back function */
          }
        }
        else
        {
          ret = -1;
        }
        frame_manager.fsm_state = FSM_COMMON_PROTOCOL_HEADER;
        break;
      }
    }

  return ret;
}


static int32_t mb_communication_ff55_protocol_package_push_chars_t(void *protocol_in, uint8_t *data, int32_t size)
{
  static commmon_protocol_frame_manager_tt frame_manager = {FSM_COMMON_PROTOCOL_HEADER};
  int32_t ret = 0;
  uint8_t c = 0;
  int32_t i = 0;
  
  communication_protocol_group_t *protocol = (communication_protocol_group_t *)(protocol_in);

  for(i = 0; i < size; i++)
  {
    c = data[i];
    switch(frame_manager.fsm_state)
    {
      case FSM_COMMON_PROTOCOL_HEADER:
      /* head byte will not be pushed */
        if(0xff == c)
        {
          frame_manager.fsm_state = FSM_COMMON_PROTOCOL_HEADER_CHECK;
        }
        else
        {
          ret = -1;
        }
      break;

      case FSM_COMMON_PROTOCOL_HEADER_CHECK:
        if(0x55 == c)
        {
          frame_manager.fsm_state = FSM_COMMON_PROTOCOL_LEN_1;
        }
        else
        {
          frame_manager.fsm_state = FSM_COMMON_PROTOCOL_HEADER;
        }
      break;

      case FSM_COMMON_PROTOCOL_LEN_1:
       {
          frame_manager.fsm_state = FSM_COMMON_PROTOCOL_DATA;
          frame_manager.data_expect_len = c;
          frame_manager.data_real_len = 0;
        }
      break;

      case FSM_COMMON_PROTOCOL_DATA:
        mb_communication_package_add_bytes_t(protocol->package, &c, 1);
        frame_manager.data_real_len++;

        if(frame_manager.data_expect_len == frame_manager.data_real_len)
        {
          if(protocol->protocol_cb)
          {
            protocol->protocol_cb(protocol->package->data, frame_manager.data_real_len); /* execute the call back function */
          }
          frame_manager.data_expect_len = 0;
          frame_manager.data_real_len = 0;
          frame_manager.fsm_state = FSM_COMMON_PROTOCOL_HEADER;
          protocol->package->data_in_begin = false;
          protocol->package->data_in_index = 0;
        }
      break;
    }
  }
  return ret;
}
static void mb_communication_protocol_set_default_t(communication_protocol_group_t *protocol)
{
  if(protocol == NULL)
  {
    return;
  }
  protocol->protocol_tag = COMMU_PROTOCOL_GROUP_NONE;
  protocol->head = 0x00;
  protocol->end = 0x00;
  protocol->protocol_cb = NULL;
  if(protocol->package)
  {
    protocol->package->data_in_begin = false;
    protocol->package->data_in_index = 0;
  }
}
