# Author: Cristian Bastidas
# Date: 06-02-2023

def solve(a: list[int], b: list[int]) -> int:

    c = []
    for num in a:
        if num in b:
            b.pop(b.index(num))
            c.append(num)

    for num in c:
        if num in a:
            a.pop(a.index(num))

    not_one = filter(lambda x: x != 1, a + b)

    return len(list(not_one))
