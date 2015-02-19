#!/bin/bash
WATCH_FILE=pins/0
FONT_NAME=epic
OS=`uname -s`

fig="figlet -w 80 -f $FONT_NAME"

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
    counter=0
    is_running=1

  elif [[ $is_running == 1 && ! -f $WATCH_FILE ]]; then
    is_running=0
  fi

  if [[ $is_running == 1 ]]; then
    counter=$((counter+1))
    fdate $counter 
  fi
done
