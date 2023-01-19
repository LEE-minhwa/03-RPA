num = 1
while num:
    if num == 20:
        break
    if num % 2 == 0:
        num += 1
        continue
    print("Hello World")
    num += 1