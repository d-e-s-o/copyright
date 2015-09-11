# range.py

#/***************************************************************************
# *   Copyright (C) 2015 Daniel Mueller (deso@posteo.net)                   *
# *                                                                         *
# *   This program is free software: you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation, either version 3 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU General Public License for more details.                          *
# *                                                                         *
# *   You should have received a copy of the GNU General Public License     *
# *   along with this program.  If not, see <http://www.gnu.org/licenses/>. *
# ***************************************************************************/

"""Functionality for handling ranges of years."""

from collections import (
  namedtuple,
)


class Range(namedtuple("Range", ["first", "last"])):
  """A class representing a time span between (but including) to years.

    A range is a tuple (first, last) of two years that mark a time span. Single
    years are represented as a tuple with the first year equal to the last
    year. Being a tuple, a Range is immutable.
  """
  def __new__(cls, first, last):
    """Create a new instance of Range."""
    if first > last:
      error = "First year ({first}) is greater than second year ({last})"
      error = error.format(first=first, last=last)
      raise ValueError(error)

    return tuple.__new__(cls, (first, last))
