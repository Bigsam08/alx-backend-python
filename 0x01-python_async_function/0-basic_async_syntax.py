#!/usr/bin/env python3
''' Async that takes in an int argument'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' create a random delay between 0 and 10 '''
    new_random = random.uniform(0, max_delay)
    await asyncio.sleep(new_random)
    return new_random
