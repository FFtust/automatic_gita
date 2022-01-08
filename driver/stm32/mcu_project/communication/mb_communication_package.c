/**   
 * \par Copyright (C), 2017-2018, MakeBlock
 * \brief   Driver for communication package group
 * @file    mb_communication_package.c
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
 * for package type
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
#include <stdlib.h>
#include <stdbool.h>

#include "mb_log.h"
#include "mb_err.h"


#include "mb_communication_package.h"

/******************************************************************************
 DEFINE MACROS
 ******************************************************************************/
#define TAG                     ("communication_package")

/******************************************************************************
 DEFINE TYPES & CONSTANTS
 ******************************************************************************/
#define PACKAGE_TYPE_POINTER_CHECK(package, ret_val) \
    if(package == NULL) \
    { \
      MB_LOGE(TAG, "%s(%d): %s", __FUNCTION__, __LINE__, "package pointer is NULL"); \
      return (ret_val); \
    }

#define PACKAGE_FULL_CHECK(package, ret_val) \
    if((package->data_in_index >= (package->buffer_size - 1))) \
    { \
      MB_LOGE(TAG, "size is %d", package->buffer_size); \
      MB_LOGE(TAG, "%s(%d): %s", __FUNCTION__, __LINE__, "package data filled"); \
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
mb_err_t mb_communication_package_show_t(communication_package_t *package)
{
	int32_t i = 0;
  PACKAGE_TYPE_POINTER_CHECK(package, MB_ERR_INVALID_ARG);

  for(i = 0; i < package->data_in_index; i++)
  {
    MB_LOGI(TAG, "package data %d  is %d", i, package->data[i]);
  }
  return MB_OK;
}

mb_err_t mb_communication_package_create_t(int32_t buffer_size, communication_package_t **package)
{
  if(buffer_size <= 0)
  {
    return MB_ERR_INVALID_ARG;
  }

  (*package) = malloc(sizeof(communication_package_t));
  memset((*package), 0, sizeof(communication_package_t));
  (*package)->data = malloc(buffer_size);
  (*package)->buffer_size = buffer_size;
  memset((*package)->data, 0, buffer_size);
  return MB_OK;
}

mb_err_t mb_communication_package_delete_t(communication_package_t *package)
{
  PACKAGE_TYPE_POINTER_CHECK(package, MB_ERR_INVALID_ARG);

  if(package->data)
  {
    free(package->data);
  }

  free(package);
  
  return MB_OK;
}

mb_err_t mb_communication_package_set_default_t(communication_package_t *package)
{
  PACKAGE_TYPE_POINTER_CHECK(package, MB_ERR_INVALID_ARG);
  package->data_in_begin = false;
  package->data_in_index = 0;
  return MB_OK;
}

mb_err_t mb_communication_package_set_channel_t(communication_package_t *package, int32_t channel)
{
  PACKAGE_TYPE_POINTER_CHECK(package, MB_ERR_INVALID_ARG);
  
  package->channel_tag = channel;
  return MB_OK;
}


mb_err_t mb_communication_package_add_bytes_t(communication_package_t *package, uint8_t *data, int32_t size)
{
	int32_t i = 0;
	uint8_t *p_temp = data;
	
  PACKAGE_TYPE_POINTER_CHECK(package, MB_ERR_INVALID_ARG);
   
  MB_LOGD(TAG, "add %d bytes", size);
  for(i = 0; i < size; i++)
  {
    PACKAGE_FULL_CHECK(package, MB_ERR_BUFFER_OVER);
    package->data[(package->data_in_index)++] = *(p_temp++);
  }
  return MB_OK;
}

uint8_t mb_communication_package_calculate_checksum_t(communication_package_t *package, int32_t start_index, int32_t mark)
{
	uint16_t i;
  uint8_t sum = 0;
  PACKAGE_TYPE_POINTER_CHECK(package, 0);
  for(i = start_index; i < package->data_in_index; i++)
  {
    sum += package->data[i];
  }
  sum = sum & mark;
  return sum;
}

mb_err_t mb_communication_package_add_checksum_t(communication_package_t *package, int32_t start_index, int32_t mark)
{
  uint8_t sum = 0;
	PACKAGE_TYPE_POINTER_CHECK(package, MB_ERR_INVALID_ARG);
  PACKAGE_FULL_CHECK(package, MB_ERR_BUFFER_OVER);
  
  sum = mb_communication_package_calculate_checksum_t(package, start_index, mark);

  package->data[(package->data_in_index)++] = sum;

  return MB_OK;
}

mb_err_t mb_communication_package_get_current_data_size_t(communication_package_t *package, int32_t *size)
{
  PACKAGE_TYPE_POINTER_CHECK(package, MB_ERR_INVALID_ARG);

  (*size) = package->data_in_index;

  return MB_OK;
}

mb_err_t mb_communication_package_get_data_t(communication_package_t *package, int32_t index, uint8_t *c)
{
  PACKAGE_TYPE_POINTER_CHECK(package, MB_ERR_INVALID_ARG);
  PACKAGE_FULL_CHECK(package, MB_ERR_BUFFER_OVER);
  
  (*c) = package->data[index];

  return MB_OK;
}

mb_err_t mb_communication_package_set_data_in_status_t(communication_package_t *package, bool status)
{
  PACKAGE_TYPE_POINTER_CHECK(package, MB_ERR_INVALID_ARG);
  
  package->data_in_begin = status;

  return MB_OK;
}

mb_err_t mb_communication_package_get_data_in_status_t(communication_package_t *package, bool *status)
{
  PACKAGE_TYPE_POINTER_CHECK(package, MB_ERR_INVALID_ARG);
  
  (*status) = package->data_in_begin;

  return MB_OK;
}
/******************************************************************************
 DEFINE PRIVATE FUNCTIONS
 ******************************************************************************/



