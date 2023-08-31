#!/usr/bin/env python3
'''
Implementation of the measure_time function
'''
import time
import asyncio
from typing import Callable


def measure_time(n: int, max_delay: int) -> float:
    '''
    Measures the total execution time for wait_n(n, max_delay) and returns
    total_time / n.

    Parameters:
    - n: The number of times to call wait_n.
    - max_delay: The maximum delay to be used in each call.

    Returns:
    - The average time per execution as a float.
    '''
    wait_n = __import__('1-concurrent_coroutines').wait_n

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    average_time_per_execution = total_time / n
    return average_time_per_execution
