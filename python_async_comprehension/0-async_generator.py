#!/usr/bin/env python3
'''
a coroutine called async_generator that takes no arguments
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Yields a random float between 0 and 10 asynchronously, 10 times.                                                                      
    '''
    for _ in range(10):
        random_num = random.uniform(0, 10)  # Using uniform for float values
        await asyncio.sleep(1)
        yield random_num
