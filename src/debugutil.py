#!/usr/bin/env python3

DEBUGGING = True

def dprint(*args, **kwargs):
    if DEBUGGING:
        print(*args, **kwargs)
