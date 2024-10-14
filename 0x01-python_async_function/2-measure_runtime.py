#!/usr/bin/env python3
''' Measure total execution time '''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Cal & return the total execution btw start time and finish time '''
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_execution = end - start
    return total_execution / n
