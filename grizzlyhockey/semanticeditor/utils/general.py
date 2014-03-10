"""
Generic utilities
"""

def any(seq):
    for i in seq:
        if i:
            return True
    return False
