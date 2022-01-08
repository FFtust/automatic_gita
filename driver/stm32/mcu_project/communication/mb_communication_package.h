/**   
 * \par Copyright (C), 2017-2018, MakeBlock
 * \brief   Header for mb_communication_package.c
 * @file    mb_communication_package.h
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
 * Header for mb_communication_package.c
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
#ifndef _MB_COMMUNICATION_PACKAGE_H_
#define _MB_COMMUNICATION_PACKAGE_H_
#include "stdint.h"
#include "stdbool.h"
#include "mb_err.h"

typedef struct
{
  uint8_t *data; // dynamic heap memory
  int32_t buffer_size;
  uint16_t data_in_begin;
  int32_t data_in_index;
  uint16_t channel_tag;
}communication_package_t;

extern mb_err_t mb_communication_package_show_t(communication_package_t *package);
extern mb_err_t mb_communication_package_create_t(int32_t buffer_size, communication_package_t **package);
extern mb_err_t mb_communication_package_delete_t(communication_package_t *package);
extern mb_err_t mb_communication_package_set_default_t(communication_package_t *package);
extern mb_err_t mb_communication_package_set_channel_t(communication_package_t *package, int32_t channel);
extern mb_err_t mb_communication_package_add_bytes_t(communication_package_t *package, uint8_t *data, int32_t size);
extern uint8_t mb_communication_package_calculate_checksum_t(communication_package_t *package, int32_t start_index, int32_t mark);
extern mb_err_t mb_communication_package_add_checksum_t(communication_package_t *package, int32_t start_index, int32_t mark);
extern mb_err_t mb_communication_package_get_current_data_size_t(communication_package_t *package, int32_t *size);
extern mb_err_t mb_communication_package_get_data_t(communication_package_t *package, int32_t index, uint8_t *c);
extern mb_err_t mb_communication_package_set_data_in_status_t(communication_package_t *package, bool status);
extern mb_err_t mb_communication_package_get_data_in_status_t(communication_package_t *package, bool *status);

#endif /* _PROCOTOL_GROUP_H_ */
