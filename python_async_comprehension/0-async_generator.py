#!/usr/bin/env python3
'''
a coroutine called async_generator that takes no arguments
'''
import asyncio
import random


async def async_generator():
    '''
    print i in a loop 10 times
    with random number from 0 to 10
    '''
    for i in range(10):
        random_num = random.randint(0, 10)
        await asyncio.sleep(1)
        yield i
