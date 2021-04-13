# SPDX-FileCopyrightText: 2021 James Carr
#
# SPDX-License-Identifier: Unlicense

from adafruit_simplemath import unconstrained_map_range


def test_unconstrained_map_range():
    assert unconstrained_map_range(-40, 32, 212, 0, 100) == -40.0
    assert unconstrained_map_range(50, 32, 212, 0, 100) == 10.0
    assert unconstrained_map_range(392, 32, 212, 0, 100) == 200.0
