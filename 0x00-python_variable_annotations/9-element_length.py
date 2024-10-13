#!/usr/bin/env python3
''' fixing the code to return the appropriate types'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' fixing the code to return the appropriate types'''
    return [(i, len(i)) for i in lst]
