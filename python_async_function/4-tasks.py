#!/usr/bin/env python3
'''
Implementation of the task_wait_n function
'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Executes task_wait_random n times asynchronously and returns
    the list of delays in ascending order.

    Parameters:
    - n: The number of times to create and run task_wait_random.
    - max_delay: The maximum delay to be used in each task.

    Returns:
    - A list of float values representing the delays.
    '''
    delay_list = await asyncio.gather(*(task_wait_random(max_delay)
                                        for _ in range(n)))
    return sorted(delay_list)
