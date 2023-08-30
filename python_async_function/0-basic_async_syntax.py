#!/usr/bin/env python3
"""basic asyncio and random lib use"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    return random delay after await"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
