/**   
 * \par Copyright (C), 2017-2018, MakeBlock
 * \brief   Driver for protocol group
 * @file    mb_protocol_group.c
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
 * for protocol type
 * \par Method List:
 *
 *
 * \par History:
 * <pre>
 * `<Author>`         `<Time>`        `<Version>`        `<Descr>`
 * fftust             2018/07/04       1.0.0              build the new.
 * </pre>
 *
 */

#include <stdint.h>
#include <string.h>
#include <stdio.h>

#include "mb_err.h"
#include "mb_log.h"
#include "mb_protocol_group.h"

/******************************************************************************
 DEFINE MACROS
 ******************************************************************************/
#define TAG                     ("protocol_group")
#define PROTOCOL_NUMBER_MAX     (64)
#define CHECK_SUM_MARK          (0x7f)

/******************************************************************************
 DEFINE TYPES & CONSTANTS
 ******************************************************************************/
#define PROTOCOL_TYPE_POINTER_CHECK(protocol, ret_val) \
    if(protocol == NULL) \
    { \
      MB_LOGE(TAG, "%s(%d): %s", __FUNCTION__, __LINE__, "protocol pointer is NULL"); \
      return (ret_val); \
    }

#define PROTOCOL_PACKAGE_FULL_CHECK(protocol, ret_val) \
    if((protocol->data_in_index >= (PACKAGE_DATA_LEN_MAX - 1))) \
    { \
      MB_LOGE(TAG, "%s(%d): %s", __FUNCTION__, __LINE__, "protocol data filled"); \
      return (ret_val); \
    }

/******************************************************************************
 DEFINE PRIVATE DATAS
 ******************************************************************************/

/******************************************************************************
 DECLARE PRIVATE FUNCTIONS
 ******************************************************************************/


/******************************************************************************
 DEFINE PUBLIC FUNCTIONS
 ******************************************************************************/
mb_err_t protocol_group_show_t(protocol_group_t *protocol)
{
  PROTOCOL_TYPE_POINTER_CHECK(protocol, MB_ERR_INVALID_ARG);

  MB_LOGI(TAG, "protocol head: %d, end: %d", protocol->head, protocol->end);
  MB_LOGI(TAG, "protocol length is %d", protocol->data_in_index);
  for(uint16_t i = 0; i < protocol->data_in_index; i++)
  {
    MB_LOGI(TAG, "protocol data %d  is %d", i, protocol->package_union.data[i]);
  }
  return MB_OK;
}

mb_err_t protocol_group_set_default_t(protocol_group_t *protocol)
{
  PROTOCOL_TYPE_POINTER_CHECK(protocol, MB_ERR_INVALID_ARG);

  protocol->head = 0x00;
  protocol->end = 0x00;
  protocol->protocol_cb = NULL;
  protocol->data_in_index = 0;
  return MB_OK;
}

mb_err_t protocol_package_push_default_t(void *protocol, uint8_t *c)
{
  PROTOCOL_TYPE_POINTER_CHECK(protocol, MB_ERR_INVALID_ARG);
  protocol_group_t *p_protocol = (protocol_group_t *)protocol;

  if(p_protocol->data_in_index >= PROTOCOL_NUMBER_MAX)
  {
    MB_LOGE(TAG, "protocol index over");
    p_protocol->data_in_begin = false;
    p_protocol->data_in_index = 0;

    return MB_ERR_INVALID_ARG;
  }
  if((*c) == p_protocol->head)
  {
    p_protocol->data_in_begin = true;
    p_protocol->data_in_index = 0;
    return MB_OK;
  }
  else if(p_protocol->data_in_begin == true)
  {
    if((*c) == p_protocol->end)
    {
      p_protocol->data_in_begin = false;
      if(protocol_package_checksum_verify_t(p_protocol, p_protocol->package_union.data[(p_protocol->data_in_index) - 1]))
      {
        MB_LOGD(TAG, "try to execute protocol cb");
        
        if(p_protocol->protocol_cb)
        {
          p_protocol->protocol_cb(p_protocol); /* execute the call back function */
        }
        return MB_OK;
      }
    }
    MB_LOGD(TAG, "protocol received data: %2x", *c);
    protocol_package_add_bytes_t(p_protocol, c, 1);
    return MB_OK;
  }
  else
  {
    return MB_FAIL;
  }
}

mb_err_t protocol_package_reset(protocol_group_t *protocol)
{
  PROTOCOL_TYPE_POINTER_CHECK(protocol, MB_ERR_INVALID_ARG);

  memset((void *)(protocol), 0, sizeof(protocol_group_t));
  return MB_OK;
}

mb_err_t protocol_package_add_bytes_t(protocol_group_t *protocol, uint8_t *data, uint16_t size)
{
  PROTOCOL_TYPE_POINTER_CHECK(protocol, MB_ERR_INVALID_ARG);
  PROTOCOL_PACKAGE_FULL_CHECK(protocol, MB_ERR_BUFFER_OVER);

  uint8_t *p_temp = data;
  for(uint16_t i = 0; i < size; i++)
  {
    protocol->package_union.data[(protocol->data_in_index)++] = *(p_temp++);
  }
  return MB_OK;
}

mb_err_t protocol_package_add_checksum_t(protocol_group_t *protocol, uint8_t mark)
{
  PROTOCOL_TYPE_POINTER_CHECK(protocol, MB_ERR_INVALID_ARG);
  PROTOCOL_PACKAGE_FULL_CHECK(protocol, MB_ERR_BUFFER_OVER);

  uint8_t sum = 0;
  for(uint16_t i = 0; i < protocol->data_in_index; i++)
  {
    sum += protocol->package_union.data[i];
  }
  protocol->package_union.data[(protocol->data_in_index)++] = sum;

  return MB_OK;
}

bool protocol_package_checksum_verify_t(protocol_group_t *protocol, uint8_t check_sum)
{
  PROTOCOL_TYPE_POINTER_CHECK(protocol, false);

  uint8_t sum = 0;
  /* head is not be contained */
  for(uint16_t i = 0; i < protocol->data_in_index - 1; i++)
  {
    sum += protocol->package_union.data[i];
  }
  sum &= 0x7f;
  if(sum == check_sum)
  {
    return true;
  }
  else
  {
    MB_LOGE(TAG, "checkesum wrong, expect:%d, real: %d", check_sum, sum);
    return false;
  }

}
/******************************************************************************
 DEFINE PRIVATE FUNCTIONS
 ******************************************************************************/



