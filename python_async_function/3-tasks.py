#!/usr/bin/env python3
'''
Implementation of the task_wait_random function
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Creates and returns an asyncio.Task for 
    wait_random with the given max_delay.

    Parameters:
    - max_delay: The maximum delay to be used in the wait_random coroutine.

    Returns:
    - An asyncio.Task object representing the asynchronous task.
    '''
    task = asyncio.create_task(wait_random(max_delay))
    return task
