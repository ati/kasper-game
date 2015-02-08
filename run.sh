#!/bin/bash
my_dir=`dirname $0`
cd $my_dir
while date; do
  ./sound_server.py | tee -a ./events.log
  sleep 2
done
