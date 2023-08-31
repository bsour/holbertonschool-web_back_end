#!/usr/bin/env python3
'''
measuring runtime for parallel comprehensions
'''
import asyncio
from typing import List
from time import perf_counter
from importlib import import_module


async_comprehension = import_module("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    '''
    Measures the total runtime for running
    async_comprehension four times in parallel.
    '''
    start_time = perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = perf_counter()
    total_runtime = end_time - start_time
    return total_runtime
