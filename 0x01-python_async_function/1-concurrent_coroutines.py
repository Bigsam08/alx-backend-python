#!/usr/bin/env python3
''' executing multiple coroutines'''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' random n times within max_delay(10) and
    return all delays in float value'''
    process = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await time for time in asyncio.as_completed(process)]
