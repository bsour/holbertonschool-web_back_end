#!/usr/bin/env python3
"""
create type-annotated functions and provide the appropriate
annotations for function arguments and return values
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with string k and square of int/float v."""
    return k, v * v
