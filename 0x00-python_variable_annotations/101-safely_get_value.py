#!/usr/bin/env python3
"""
Safely retrieves a value from a dictionary based on a key.
"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: T = None) -> Union[Any, T]:
    """
    Retrieves a value from a dict using a given key.
    """
    if key in dct:
        return dct[key]
    else:
        return default
