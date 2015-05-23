#!/bin/bash
ROOM_ID=19
WATCH_FILE=pins/0
FONT_NAME=epic
OS=`uname -s`

fig="figlet -w 80 -f $FONT_NAME"
cd `dirname $0`

function fdate()
{
  seconds=${1:0}
  clear
  echo -e "\n"

  if [[ $OS == "Linux" ]]; then
    date +"  %H:%M:%S" --date="1970-01-01 $seconds seconds" | $fig
  else
    #BSD date
    date -f%s -u -j +"  %H:%M:%S" $seconds | $fig
  fi
}

counter=0
is_running=1
fdate $counter

while sleep 1; do

  if [[ $is_running == 0 && -f $WATCH_FILE ]]; then
    # start game
    counter=0
    is_running=1
    echo "start" >> api_events.log
    date >> api_events.log
    ./start $ROOM_ID >> api_events.log

  elif [[ $is_running == 1 && ! -f $WATCH_FILE ]]; then
    # stop game
    is_running=0
    echo "stop" >> api_events.log
    date >> api_events.log
    # ./stop $ROOM_ID >> api_events.log
  fi

  if [[ $is_running == 1 ]]; then
    counter=$((counter+1))
    fdate $counter 
  fi
done
