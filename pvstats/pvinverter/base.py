#!/usr/bin/env python

# Based on xxx from yyy

# Copyright 2018 Paul Archer
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pymodbus.constants import Defaults
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.transaction import ModbusSocketFramer

class BasePVInverter(ModbusTcpClient):
  def __init__(self, host='127.0.0.1', port=Defaults.Port,
               framer=ModbusSocketFramer, **kwargs):
    super(BasePVInverter, self).__init__(host, port, framer, **kwargs)
    self.registers = {}

#-----------------
# Exported symbols
#-----------------
__all__ = [
  "BasePVInverter"
]

# vim: set expandtab ts=2 sw=2:
