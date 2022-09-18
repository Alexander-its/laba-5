a = 0
s = 0
while True:
    a = int(input())
 
    if a == 0:
        break
    elif a < 0:
        s += 1
print(s)
