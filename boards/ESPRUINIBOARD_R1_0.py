#!/bin/false
# This file is part of Espruino, a JavaScript interpreter for Microcontrollers
#
# Copyright (C) 2013 Gordon Williams <gw@pur3.co.uk>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# ----------------------------------------------------------------------------------------
# This file contains information for a specific board - the available pins, and where LEDs,
# Buttons, and other in-built peripherals are. It is used to build documentation as well
# as various source and header files for Espruino.
# ----------------------------------------------------------------------------------------

import pinutils;
info = {
 'name' : "Espruini Board rev 1.0",
 'link' : [ "http://www.espruino.com/EspruinoBoard" ],
 'default_console' : "EV_SERIAL1",
 'default_console_tx' : "B6",
 'default_console_rx' : "B7",
 'variables' : 3040,
 'binary_name' : 'espruino_%v_espruini_1r0.bin',
};
chip = {
  'part' : "STM32F401CCU6",
  'family' : "STM32F4",
  'package' : "UQFN48", 
  'ram' : 64,
  'flash' : 256,
  'speed' : 84,
  'usart' : 3,
  'spi' : 3,
  'i2c' : 3,
  'adc' : 1,
  'dac' : 0,
  'saved_code' : {
    'address' : 0x08004000,
    'page_size' : 16384, # size of pages
    'page_number' : 1, # number of page we start at (0 based)
    'pages' : 3, # number of pages we're using
    'flash_available' : 256 # binary will have a hole in it, so we just want to test against full size
  },
  'place_text_section' : 0x08010000, # note flash_available above
};
# left-right, or top-bottom order
board = {
  'left' : [ 'GND', '3V3', 'BOOT0', 'NRST' ],
#  'left2' : [ 'GND', 'A12', 'A11', 'VCC' ],
  'top' : [ '5V', 'A13', 'A14', 'A15',  'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'],
  'bottom' : [ 'GND','BAT_IN','B15', 'B14', 'B13', 'B10', 'B2', 'B1', 'A7', 'A6', 'A5' ], 


  'right2' : ['A9','A0','A1','A3'],
  'right' : ['A10','A8','A2','A4'],        
};
devices = {
  'OSC' : { 'pin_in' :  'H0', # checked
            'pin_out' : 'H1' }, # checked
  'OSC_RTC' : { 'pin_in' :  'C14', # checked
                'pin_out' : 'C15' }, # checked
  'BTN1' : { 'pin' : 'C13', 'pinstate' : 'IN_PULLDOWN' }, 
  'LED1' : { 'pin' : 'B12' }, 
  'LED2' : { 'pin' : 'B2' },
  'USB' : { 'pin_charge' :  'B0',
            'pin_vsense' :  'B1',
            'pin_dm' : 'A11',   # checked
            'pin_dp' : 'A12' }, # checked
  'JTAG' : {
        'pin_MS' : 'A13',
        'pin_CK' : 'A14', 
        'pin_DI' : 'A15' 
          }
};

board_css = """
#board {
  width: 835px;
  height: 365px;
  top: 200px;
  left : 100px;
  background-image: url(img/ESPRUINIBOARD_R1_0.png);
}
#boardcontainer {
  height: 585px;
}
#left {
  top: 105px;
  right: 560px;  
}
#left2  {
  top: 105px;
  left: -100px;
}
#top {
  bottom: 320px;
  left: 240px;
}
#bottom {
  top: 320px;
  left: 240px;
}

#right  {
  top: 105px;
  left: 820px;
}
#right2  {
  top: 105px;
  right: 105px;
}

.leftpin { height: 48px; }
.left2pin { height: 48px; }
.toppin { width: 48px; }
.bottompin { width: 48px; }

.rightpin { height: 48px; }
.right2pin { height: 48px; }

""";

def get_pins():
  pins = pinutils.scan_pin_file([], 'stm32f401.csv', 5, 8, 9)
  return pinutils.only_from_package(pinutils.fill_gaps_in_pin_list(pins), chip["package"])