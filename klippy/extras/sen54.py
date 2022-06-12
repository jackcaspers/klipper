# Support for i2c based temperature sensors
#
# Copyright (C) 2020  Eric Callahan <arksine.code@gmail.com>
#
# This file may be distributed under the terms of the GNU GPLv3 license.
import logging
from . import bus

SEN54_CHIP_ADDR = 0x76

SEN54_REGS = {'START_M': 0x0021, 'START_M_RHT': 0x0037}

# Need to determine registers that are being used 
# Need to be able to read from those registers
# Need to handle those registers in a way that makes sense
# Create proper logic to parse data
# Determine any other constants

class SEN54:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.chip_type = 'SEN54'
        self.chip_address = SEN54_CHIP_ADDR
        self.i2c = bus.MCU_I2C_from_config(
            config, default_addr=SEN54_CHIP_ADDR, default_speed=100000)


def load_config(config):
    # Register sensor
    pheaters = config.get_printer().load_object(config, "heaters")