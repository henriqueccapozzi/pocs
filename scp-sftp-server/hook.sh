#! /bin/sh
if [ "$PAM_TYPE" == "close_session" ];then
    exit 0
fi


LOG_FILE="/tmp/log"
export TZ=UTC+3

echo "$(date +'[%F %H:%M:%S%z]' | tr -d $'\n') - Accessed from host ($PAM_RHOST) by user ($PAM_USER)" >> ${LOG_FILE}
