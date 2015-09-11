#!/usr/bin/env python

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

"""A test suite for the Range class."""

from deso.copyright import (
  Range,
)
from unittest import (
  main,
  TestCase,
)


class TestRange(TestCase):
  """Tests for the Range class."""
  def testCreationSucceedsForValidRange(self):
    """Verify that creation of a Range object succeeds for valid ranges."""
    Range(2015, 2015)
    Range(2014, 2015)
    Range(2013, 2015)


  def testCreationFailsIfYearsNotOrdered(self):
    """Verify that creation of a range with the first year greater than the last fails."""
    first = 2014
    last = 2013
    regex = r"%d.*is greater than.*%d" % (first, last)

    with self.assertRaisesRegex(ValueError, regex):
      Range(first, last)


if __name__ == "__main__":
  main()
