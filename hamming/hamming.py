import typing

def distance(strand_a: str, strand_b: str) -> int:
    
    if len(strand_a) != len(strand_b):
        raise ValueError("Different sizes")
    
    count = 0
    for (a, b) in zip(strand_a, strand_b):
        if a != b:
            count+=1

    return count
