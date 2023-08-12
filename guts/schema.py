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

from __future__ import annotations

from typing import Any, TypeVar, Type, List

from dataclasses import dataclass, field, MISSING
import dataclasses

import warnings

from guts._utils import get_type_annotations


############################################################################
# Schema Warning and Errors
############################################################################
class UnknownSchemaChild(RuntimeWarning):
  """Warning for when parsing a schema and an unknown child is found"""
  pass


class MissingRequiredSchemaChild(TypeError):
  """Error when a schema is missing a required child"""
  pass


############################################################################
# Base Schema
############################################################################
SchemaBaseT = TypeVar("SchemaBaseT", bound="_SchemaBase")


@dataclass
class _SchemaBase:
  @classmethod
  def from_dict(cls: Type[SchemaBaseT], definition: dict) -> SchemaBaseT:
    """Create the schema object from a dictiontary definition.

    Args:
        cls (Type[SchemaBaseT]): The class to create
        definition (dict): The dictionary definition to create the schema from

    Returns:
        SchemaBaseT: The Schema object which is generated
    """
    kwargs = {}

    type_annotations = get_type_annotations(cls)

    for fld in dataclasses.fields(cls):
      if fld.name in definition:
        ftype = type_annotations[fld.name]

        if issubclass(ftype, _SchemaBase):
          kwargs[fld.name] = ftype.from_dict(definition[fld.name])
        elif f"{fld.name}_formatter" in dir(cls):
          kwargs[fld.name] = getattr(cls, f"{fld.name}_formatter")(definition[fld.name])
        elif f"{fld.type}_formatter" in dir(cls):
          kwargs[fld.name] = getattr(cls, f"{fld.type}_formatter")(definition[fld.name])
        else:
          kwargs[fld.name] = ftype(definition[fld.name])

      elif fld.default is MISSING and fld.default_factory is MISSING:
        raise MissingRequiredSchemaChild(
                f"{cls.__name__} schema missing required child: {fld.name}"
              )

    for child in definition:
      if child not in [fld.name for fld in dataclasses.fields(cls)]:
        warnings.warn(f"{cls.__name__} schema found unknown child: {fld.name}", UnknownSchemaChild)

    return cls(**kwargs)


############################################################################
# Base Schema
############################################################################
@dataclass
class Param(_SchemaBase):
  """A Schema object which represents a parameter"""

  name: str
  """The name of the parameter"""
  type: str
  """The type of the parameter"""
  value: str
  """The value of the parameter"""
  range: List[str] = field(default_factory=list)
  """The valid ranges of the parameter"""


@dataclass
class Sequence(_SchemaBase):
  """A Schema object which represents a UVM Sequence"""

  name: str
  """The name of the sequence"""
  param: Param
  """A list of parameters for the sequence"""
  timeout: int
  """The timeout of the sequence in ns"""

  @staticmethod
  def name_formatter(raw_name: Any) -> str:
    """Derive the name of the Sequence from an original unformatted name.

    Args:
        raw_name (Any): The raw name of the string

    Returns:
        str: The formatted string name
    """
    if not isinstance(raw_name, str):
      raise TypeError("Sequence schema name is not a string")
    return raw_name.replace(" ", "_")

  @staticmethod
  def int_formatter(raw_int: int | str) -> int:
    """Derive an int for this Schema from the original unformatted int

    Args:
        raw_int (int | str): The integer to derive from

    Returns:
        int: The derived integer
    """
    if isinstance(raw_int, int):
      return raw_int

    if not isinstance(raw_int, str):
      raise TypeError("Sequence int formatter did not recieve int or string")

    raw_int = raw_int.strip()

    if raw_int.startswith(("0x", "0X",)):
      return int(raw_int, base=16)
    if raw_int.startswith(("x", "X")):
      return int(raw_int[1:], base=16)
    if "'h" in raw_int:
      substr = raw_int.find("'h") + len("'h")
      return int(raw_int[substr:], 16)

    return int(raw_int)
