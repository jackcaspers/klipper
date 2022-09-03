# Support for i2c based temperature sensors
#
# Copyright (C) 2020  Eric Callahan <arksine.code@gmail.com>
#
# This file may be distributed under the terms of the GNU GPLv3 license.
import logging
from . import bus

SEN54_CHIP_ADDR = 0x76

SEN54_REGS = {
    'START_M': 0x0021, 
    'START_M_RHT': 0x0037,
    'STOP_M': 0x0104,
    'READ_DATA_FlAG': 0x0202,
    'READ_M_VALUES': 0x03C4,
    'RW_TEMP_COMP_PARAM': 0x60B2,
    'RW_WARM_START_PARAM': 0x60C6,
    'RW_VOC_ALGO_TUNE': 0x60D0,
    'RW_NOX_ALGO_TUNE': 0x60E1,
    'RW_RHT_ACC_MODE': 0x60F7,
    'RW_VOC_ALGO_STATE': 0x6181,
    'START_FAN_CLEANING': 0x5607,
    'RW_AUTO_CLEANING_INTERVAL': 0x8004,
    'READ_PRODUCT_NAME': 0xD014,
    'READ_SERIAL_NUMBER': 0xD033,
    'READ_FIRM_VERSION': 0xD100,
    'READ_DEVICE_STATUS': 0xD206,
    'CLEAR_DEVICE_STATUS': 0xD210,
    'RESET': 0xD304
}

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