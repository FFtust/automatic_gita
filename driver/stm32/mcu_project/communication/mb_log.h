/**   
 * \par Copyright (C), 2017-2018, MakeBlock
 * \brief   system log config, for platform irrelevant module
 * @file    mb_log.h
 * @author  fftust
 * @version V1.0.0
 * @date    2018/06/08
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
 * This file define the system logs function, for platform irrelevant module
 * \par Method List:
 *
 *
 * \par History:
 * <pre>
 * `<Author>`         `<Time>`        `<Version>`        `<Descr>`
 * fftust             2018/06/08      1.0.0              build the new.
 * </pre>
 *
 */
#ifndef _MB_LOG_H_
#define _MB_LOG_H_

#define MB_LOG_NONE     0
#define MB_LOG_ERROR    1
#define MB_LOG_WARNING  2
#define MB_LOG_INFO     4
#define MB_LOG_DEBUG    5
#define MB_LOG_VERBOSE  6

#define MB_LOG_LEVEL ESP_LOG_INFO
#define MB_LOGE( tag, format, ... )  // if (MB_LOG_LEVEL >= ESP_LOG_ERROR)   { esp_log_write(ESP_LOG_ERROR,   tag, LOG_FORMAT(E, format), esp_log_timestamp(), tag, ##__VA_ARGS__); }
#define MB_LOGW( tag, format, ... )  // if (MB_LOG_LEVEL >= ESP_LOG_WARN)    { esp_log_write(ESP_LOG_WARN,    tag, LOG_FORMAT(W, format), esp_log_timestamp(), tag, ##__VA_ARGS__); }
#define MB_LOGI( tag, format, ... )  // if (MB_LOG_LEVEL >= ESP_LOG_INFO)    { esp_log_write(ESP_LOG_INFO,    tag, LOG_FORMAT(I, format), esp_log_timestamp(), tag, ##__VA_ARGS__); }
#define MB_LOGD( tag, format, ... )  // if (MB_LOG_LEVEL >= ESP_LOG_DEBUG)   { esp_log_write(ESP_LOG_DEBUG,   tag, LOG_FORMAT(D, format), esp_log_timestamp(), tag, ##__VA_ARGS__); }
#define MB_LOGV( tag, format, ... )  // if (MB_LOG_LEVEL >= ESP_LOG_VERBOSE) { esp_log_write(ESP_LOG_VERBOSE, tag, LOG_FORMAT(V, format), esp_log_timestamp(), tag, ##__VA_ARGS__); }


#endif /* _MB_LOG_H_ */
