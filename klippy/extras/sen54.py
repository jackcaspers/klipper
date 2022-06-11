# Support for i2c based temperature sensors
#
# Copyright (C) 2020  Eric Callahan <arksine.code@gmail.com>
#
# This file may be distributed under the terms of the GNU GPLv3 license.
import logging
from . import bus

SEN54_CHIP_ADDR = 0x76

class SEN54:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.chip_type = 'SEN54'
        self.chip_address = SEN54_CHIP_ADDR


def load_config(config):
    # Register sensor
    pheaters = config.get_printer().load_object(config, "heaters")