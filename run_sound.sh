#!/bin/bash
my_dir=`dirname $0`
cd $my_dir

mkdir -p pins
rm -rf ./pins/*

sudo pkill -f "demo_thanks" && sleep 2
while date; do
  sudo ./sound_server.py >> ./events.log
done
