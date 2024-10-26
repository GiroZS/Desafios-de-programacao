import math

def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def arvores_minimas(N, positions):
    positions.sort()

    dif = [positions[i+1] - positions[i] for i in range(N-1)]

    overall_mdc = dif[0]
    for diff in dif[1:]:
        overall_mdc = mdc(overall_mdc, diff)

    additional_trees = 0
    for diff in dif:
        additional_trees += (diff // overall_mdc) - 1

    return additional_trees
positions=[]
N = int(input())
for i in range(N):
    positions.append(int(input()))
print(arvores_minimas(N, positions))  