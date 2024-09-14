# 計算1到100的總和
total = 0
for i in range(1, 101):
    total += i
print(total)


# 使用while迴圈計算1到100的總和
total = 0
counter = 1

while counter <= 100:
    total += counter
    counter += 1

print(f"使用while迴圈計算的1到100總和為: {total}")

