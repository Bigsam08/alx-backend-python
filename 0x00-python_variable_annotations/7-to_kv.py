#!/usr/bin/env python3
''' A function that takes a string and int OR float to return a tupple'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v**2))
