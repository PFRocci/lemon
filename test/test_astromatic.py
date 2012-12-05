#! /usr/bin/env python

# Copyright (c) 2012 Victor Terron. All rights reserved.
# Institute of Astrophysics of Andalusia, IAA-CSIC
#
# This file is part of LEMON.
#
# LEMON is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import random
import unittest

from astromatic import Pixel

NITERS = 100

class PixelTest(unittest.TestCase):

    X_COORD_RANGE = (1, 2048)
    Y_COORD_RANGE = (1, 2048)

    @classmethod
    def random(cls):
        """ Return a random Pixel object """
        x = random.uniform(*cls.X_COORD_RANGE)
        y = random.uniform(*cls.Y_COORD_RANGE)
        return Pixel(x, y)

    def test_init(self):
        for _ in xrange(NITERS):
            x = random.uniform(*self.X_COORD_RANGE)
            y = random.uniform(*self.Y_COORD_RANGE)
            pixel = Pixel(x, y)
            self.assertEqual(pixel.x, x)
            self.assertEqual(pixel.y, y)

    def test_repr(self):
        for _ in xrange(NITERS):
            pixel = self.random()
            repr_pixel = eval(`pixel`)

            # We need to use TestCase.assertAlmostEqual, instead of a simple
            # equality comparison, because the precision of the coordinates in
            # 'repr_pixel' is limited by the number of decimal places printed
            # by __repr__. The Pixel returned by eval(`pixel`), therefore, may
            # not be exactly equal to 'pixel' when the coordinates are real
            # numbers, but we just want to verify that it __repr__ computes a
            # valid, approximate-enough string representation of the object.

            kwargs = dict(places = 5)
            self.assertAlmostEqual(pixel.x, repr_pixel.x, **kwargs)
            self.assertAlmostEqual(pixel.y, repr_pixel.y, **kwargs)

