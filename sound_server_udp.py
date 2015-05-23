#!/usr/bin/env python
import sys
import logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(message)s')

import json
import socket
import pygame
import re
import os

PINS = 11
ACTIVE = '0'
UDP_IP = '0.0.0.0'
UDP_PORT = 40000


pins = {
  'current_state': ['1']*PINS,
  'sounds': [None]*PINS,
  'modes': [None]*PINS
}


def handle_state(new_state):
  for idx, state_bit in enumerate(new_state):
    if not pins['sounds'][idx]:
      continue

    if (pins['current_state'][idx] == state_bit):
      continue
    else:
      logging.info("state of pin %d changed from %s to %s"%(idx, pins['current_state'][idx], state_bit))
      snd = pins['sounds'][idx]

      if pins['modes'][idx] == 'hold':
        fname="pins/%d"%idx
        try:
          if (state_bit == ACTIVE):
            open(fname, 'a').close() # touch file with name=pin number
            snd.play(-1) 
          else:
            os.remove(fname)
            snd.stop()
        except:
          logging.error(sys.exc_info()[0])

      else:
        if (state_bit == ACTIVE):
          snd.play()

      pins['current_state'][idx] = state_bit


def main():
  config = json.load(open('config.json'));
#  pygame.mixer.init(config['frequency'], config['size'], config['channels'])

  sock = socket.socket(socket.AF_INET, # Internet
    socket.SOCK_DGRAM) # UDP
  sock.bind((UDP_IP, UDP_PORT))

  logging.info("Sound server initialized, waiting for UDP messages")

# Event: key: key_pressed
# type: radiobutton
# quest_id: 1
# key_id: 4: 74
  while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    logging.info("received message: '%s'"%data)
    strings = [ s.strip() for s in data.splitlines() ]

    if (not strings[0].capitalize().startswith('Event')):
      print "Skipping unknown message from ", addr
      continue

    kws = {}
    for part in map(lambda x: x.split(':', 1), strings):
      kws[part[0]] = part[1].strip() if part[1] else None

    print kws

    #instr = re.sub('[^01]', '', instr).zfill(PINS)
    #handle_state(list(instr)[0:PINS])
        


main()
