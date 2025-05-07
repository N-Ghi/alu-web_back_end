#!/usr/bin/env python3

def make_multiplier (multiplier : float):
    def multiply(n : float):
        return n * multiplier
    return multiply