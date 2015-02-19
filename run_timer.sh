#!/bin/bash
WATCH_FILE=pins/3
FONT_NAME=epic
OS=`uname -s`

function fdate()
{
  seconds=${1:0}
  if [[ $OS == "Linux" ]]; then
    date +"  %H:%M:%S" --date="1970-01-01 $seconds seconds"
  else
    #BSD date
    date -f%s -u -j +"  %H:%M:%S" $seconds
  fi
}

counter=0
is_running=1

while sleep 1; do

  if [[ $is_running == 0 && -f $WATCH_FILE ]]; then
    counter=0
    is_running=1

  elif [[ $is_running == 1 && ! -f $WATCH_FILE ]]; then
    is_running=0
  fi


  if [[ $is_running == 1 ]]; then
    counter=$((counter+1))
    clear
    echo -e "\n"
    fdate $counter | figlet -w 80 -f $FONT_NAME
  fi
done
