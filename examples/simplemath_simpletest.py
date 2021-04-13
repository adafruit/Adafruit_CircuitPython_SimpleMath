# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

from adafruit_simplemath import map_range, constrain

print("map_range() examples")
# Map, say, a sensor value, from a range of 0-255 to 0-1023.
sensor_input_value = 30
sensor_converted_value = map_range(sensor_input_value, 0, 255, 0, 1023)
print(
    "Sensor input value:",
    sensor_input_value,
    "Converted value:",
    sensor_converted_value,
)

percent = 23
screen_width = 320  # or board.DISPLAY.width
x = map_range(percent, 0, 100, 0, screen_width - 1)
print("X position", percent, "% from the left of screen is", x)

celsius = 20
fahrenheit = map_range(celsius, 0, 100, 32, 212, constrained=False)
print(celsius, "degress Celsius =", fahrenheit, "degrees Fahrenheit")

celsius = -20
fahrenheit = map_range(celsius, 0, 100, 32, 212, False)
print(celsius, "degress Celsius =", fahrenheit, "degrees Fahrenheit")

print("constrain() examples")
# Constrain a value to a range.
def constrain_example(value, min_value, max_value):
    constrained_value = constrain(value, min_value, max_value)
    print(
        "Constrain",
        value,
        "between [",
        min_value,
        "and",
        max_value,
        "] gives",
        constrained_value,
    )


constrain_example(0, 1, 3)  # expects 1
constrain_example(4, 1, 3)  # expects 3
constrain_example(2, 2, 3)  # expects 2
