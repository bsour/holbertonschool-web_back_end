#!/usr/bin/env python3
"""
A module that contains a function to measure runtime
"""
import asyncio
import time
from typing import List
from random import uniform
from importlib import import_module

async_comprehension = import_module("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime for running
    async_comprehension four times in parallel.
    """
    start_time = time.time()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
