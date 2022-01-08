/**   
 * \par Copyright (C), 2017-2018, MakeBlock
 * \brief   error type definition, for platform irrelevant module
 * @file    mb_err.h
 * @author  fftust
 * @version V1.0.0
 * @date    2018/06/8
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
 * This file define the error types, mainly used for debuging, platform irrelevant module
 *
 * \par Method List:
 *
 *
 * \par History:
 * <pre>
 * `<Author>`         `<Time>`        `<Version>`        `<Descr>`
 *  fftust            2018/05/22      1.0.0              build the new.
 * </pre>
 *
 */

#ifndef _MB_ERR_H_
#define _MB_ERR_H_

#include "stdint.h"

/******************************************************************************
 DEFINE MACROS
 ******************************************************************************/
#define MB_OK                      (0)
#define MB_FAIL                    (-1)
 
#define MB_ERR_NO_MEM              (0x101)
#define MB_ERR_INVALID_ARG         (0x102)
#define MB_ERR_INVALID_STATE       (0x103)
#define MB_ERR_INVALID_SIZE        (0x104)
#define MB_ERR_NOT_FOUND           (0x105)
#define MB_ERR_NOT_SUPPORTED       (0x106)
#define MB_ERR_TIMEOUT             (0x107)
#define MB_ERR_INVALID_RESPONSE    (0x108)
#define MB_ERR_BUFFER_OVER         (0x109)
#define MB_ERR_INVALID_VERSION     (0x10A)
#define MB_ERR_INVALID_MAC         (0x10B)

#define FUNCTION_RET_CHECK(a, str, ret_val) \
    if((a)) \
    { \
      MB_LOGE(TAG, "%s(%d):err_id(%d), %s", __FUNCTION__, __LINE__, a, str); \
      return (ret_val); \
    }

#define FUNCTION_RET_CHECK_WITHOUT_RETURN(a, str, ret_val) \
    if((a)) \
    { \
      MB_LOGE(TAG, "%s(%d):err_id(%d), %s", __FUNCTION__, __LINE__, a, str); \
    }

/******************************************************************************
 DEFINE TYPES & CONSTANTS
 ******************************************************************************/
typedef int32_t mb_err_t;

#endif /* _MB_ERR_H_ */