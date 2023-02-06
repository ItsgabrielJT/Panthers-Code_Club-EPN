# Author: Cristian Bastidas
# Date: 06-02-2023

def solve(a: list[int]) -> int:

    if len(a) == 0:
        return 0

    for i in range(1, len(a)):
        while a[0] < a[i]:
            a[0] += 1
            a[i] -= 1

    return a[0]
