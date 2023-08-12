############################################################################
# Library/Tool for automatic generate of UVM tests and support files       #
# Copyright (C) 2023  RISCY-Lib Contributors                               #
#                                                                          #
# This library is free software; you can redistribute it and/or            #
# modify it under the terms of the GNU Lesser General Public               #
# License as published by the Free Software Foundation; either             #
# version 2.1 of the License, or (at your option) any later version.       #
#                                                                          #
# This library is distributed in the hope that it will be useful,          #
# but WITHOUT ANY WARRANTY; without even the implied warranty of           #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU        #
# Lesser General Public License for more details.                          #
#                                                                          #
# You should have received a copy of the GNU GLesser eneral Public License #
# along with this program.  If not, see <https://www.gnu.org/licenses/>.   #
############################################################################

import pytest

from guts.schema import Param, Sequence


@pytest.mark.parametrize("name,type,value", [
  ("test",        "int", 32),
  ("hello_world", "bit", "1'b0")
])
def test_schema_param(name, type, value):
  p = Param.from_dict({
        "name": name,
        "type": type,
        "value": value
      })

  assert p.name == name
  assert p.type == type
  assert p.value == str(value)


@pytest.mark.parametrize("name,param,timeout,timeout_int", [
  ("test",        {"name": "testname", "type": "int", "value": "1"}, 32, 32),
  ("hello world", {"name": "testname", "type": "int", "value": "1"}, "'hB3A", 0xB3A),
  ("hello world", {"name": "testname", "type": "int", "value": "1"}, "32'hB3A", 0xB3A),
  ("hello world", {"name": "testname", "type": "int", "value": "1"}, "0xB3A", 0xB3A),
  ("hello world", {"name": "testname", "type": "int", "value": "1"}, "xB3A", 0xB3A)
])
def test_schema_sequence(name, param, timeout, timeout_int):
  s = Sequence.from_dict({
        "name": name,
        "param": param,
        "timeout": timeout
      })

  assert s.name == name.replace(" ", "_")
  assert s.param.name == param["name"]
  assert s.param.type == param["type"]
  assert s.param.value == param["value"]
  assert s.timeout == timeout_int
