#!/usr/bin/env python3
''' Augumenet code with correct duck-typed annotations'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' Augumenet code with correct duck-typed annotations'''
    if lst:
        return lst[0]
    else:
        return None
