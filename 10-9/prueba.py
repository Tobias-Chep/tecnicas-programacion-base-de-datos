import time

for t in range(10, -1, -1):
    print(t)
    t -= 1
    time.sleep(1)
    if t <= 0:
        print(t)
        print("¡BUM!")
        break