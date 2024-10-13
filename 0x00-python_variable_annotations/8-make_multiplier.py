#!/usr/bin/env python3
''' Function that takes an arg float and returns a function that
multiplies a float'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier
