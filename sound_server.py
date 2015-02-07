#!/usr/bin/env python
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

import json
import serial
import pygame
import re

ACTIVE = '0'

pins = {
  'current_state': ['1']*8,
  'sounds': [None]*8,
  'modes': [None]*8
}


def init_pins(pin_cfg):
  for i in range(0,min(8,len(pin_cfg))):
    pins['sounds'][i] = pygame.mixer.Sound('sounds/' + pin_cfg[i]['snd_file'])
    pins['modes'][i] = pin_cfg[i]['mode']
  # pins['sounds'][0].play()


def handle_state(new_state):
  for idx, state_bit in enumerate(new_state):
    if (pins['current_state'][idx] == state_bit):
      continue
    else:
      logging.info("state of pin %d changed from %s to %s"%(idx, pins['current_state'][idx], state_bit))
      snd = pins['sounds'][idx]

      if pins['modes'][idx] == 'hold':
        snd.play(-1) if (state_bit == ACTIVE) else snd.stop()
      else:
        if (state_bit == ACTIVE):
          snd.play()

      pins['current_state'][idx] = state_bit


def main():
  config = json.load(open('config.json'));
  arduino = serial.Serial(config['arduino'], 115200);
  pygame.mixer.init(config['frequency'], config['size'], config['channels'])
  init_pins(config['pins'])

  logging.info("Sound server initialized, waiting for Arduino commands")
  while True:
    instr = arduino.readline()
    logging.info("received: '%s'"%instr)
    instr = re.sub('[^\d]', '', instr).zfill(8)
    handle_state(list(instr))
        


main()
