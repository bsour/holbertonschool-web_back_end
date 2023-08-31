#!/usr/bin/env python3
'''
collect 10 random numbers using an async comprehension
and return random numbers
'''
import asyncio
from typing import List
from random import uniform
from importlib import import_module

# Import async_generator using import_module
async_generator = import_module("0-async_generator").async_generator

async def async_comprehension() -> List[float]:
    '''
    collects 10 random number using async comp
    '''
    return [x async for x in async_generator()]
