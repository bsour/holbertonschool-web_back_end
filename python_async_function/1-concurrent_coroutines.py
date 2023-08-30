#!/usr/bin/env python3
"""import method wait_random and spawn wait random n times"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times asynchronously and returns
    the list of delays in ascending order.

    Parameters:
    - n: The number of times to call wait_random.
    - max_delay: The maximum delay to be used in each call.

    Returns:
    - A list of float values representing the delays.
    """
    delay_list = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delay_list)
