# hw09
for i in range(1,10):
    for j in range(1,10):
        if i * j > 10:
            print(f"First pair: {i}*{j}")
            break
    else:
        continue
    break