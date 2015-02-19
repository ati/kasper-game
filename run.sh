#!/bin/bash

# trap ctrl-c and call ctrl_c()
trap ctrl_c INT

function ctrl_c()
{
  echo "** Trapped CTRL-C"
  if [[ ! -z "$sound_pid" ]]; then
    sudo pkill $sound_pid
  fi
}


cd `dirname $0`
echo "starting sound server..."
./run_sound.sh &
sound_pid=$!

sleep 2
echo "starting timer..."
sleep 2
./run_timer.sh
