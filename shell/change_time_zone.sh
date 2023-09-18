#!/bin/bash

##
# 脚本注释： 此脚本用来修改本机的时区为指定时区
##

function check() 
{
    catch_str=`timedatectl list-timezones | grep $1`
    echo "查询结果 $catch_str"
    if [ -z "$catch_str" ];
    then
        return 0;
    fi

    return 1;
}

function change()
{
    time_zone=$1
    timedatectl set-timezone $time_zone
}

function main()
{
    # 时区
    target_time_zone_name=$1
    echo "目标时区: $target_time_zone_name"
    echo 'before'
    echo `timedatectl | grep 'Time zone'`
    check $target_time_zone_name
    ret=$?
    if [ $ret -eq 0 ];
    then
        echo '不存在的时区，请使用 commond: timedatectl list-timezones 查看所以的时区'
        exit -1
    fi
    change $target_time_zone_name
    echo 'after'
    echo `timedatectl | grep 'Time zone'`
    exit 0
}


#####################################################

main $@