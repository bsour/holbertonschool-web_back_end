#!/usr/bin/env python3
'''
a coroutine called async_generator that takes no arguments
'''
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''
    print i in a loop 10 times
    with random number from 0 to 10
    '''
    for _ in range(10):
        random_num = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield random_num
