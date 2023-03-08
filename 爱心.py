import math

def print_heart():
for y in range(15, -15, -1):
for x in range(-30, 30):
if math.pow(math.pow(x * 0.04, 2) + math.pow(y * 0.1, 2) - 1, 3) - math.pow(x * 0.04, 2) * math.pow(y * 0.1, 3) <= 0:
print("*", end="")
else:
print(" ", end="")
print()

print_heart()