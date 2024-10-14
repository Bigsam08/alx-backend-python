#!/usr/bin/env python3
''' Altering code from file to a file'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' finish the job '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
