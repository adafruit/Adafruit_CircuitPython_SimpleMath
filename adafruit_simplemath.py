# SPDX-FileCopyrightText: Copyright (c) 2021 Dan Halbert for Adafruit Industries LLC
#
# SPDX-License-Identifier: MIT
"""
`adafruit_simplemath`
================================================================================

Math utility functions


* Author(s): Adafruit Industries

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_SimpleMath.git"


def map_range(x, in_min, in_max, out_min, out_max):
    """
    Maps a number from one range to another. Somewhat similar to the Arduino ``map()`` function, but
    returns a floating point result, and constrains the output value to be between ``out_min`` and ``out_max``.

    :return: Returns value mapped to new range
    :rtype: float
    """
    in_range = in_max - in_min
    in_delta = x - in_min
    if in_range != 0:
        mapped = in_delta / in_range
    elif in_delta != 0:
        mapped = in_delta
    else:
        mapped = 0.5
    mapped *= out_max - out_min
    mapped += out_min
    if out_min <= out_max:
        return max(min(mapped, out_max), out_min)
    return min(max(mapped, out_max), out_min)


def constrain(x, out_min, out_max):
    """Constrains ``x`` to be within the inclusive range ``[out_min, out_max]``.
    Sometimes called ``clip`` or ``clamp`` in other libraries.
    ``out_min`` should be less than or equal to ``out_max``.
    If ``x`` is less than ``out_min``, return ``out_min``.
    If ``x`` is greater than ``out_max``, return ``out_max``.
    Otherwise just return ``x``.

    :return: Returns value constrained to given range
    """
    return max(out_min, min(x, out_max))
