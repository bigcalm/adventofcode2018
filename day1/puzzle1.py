f = open('input.txt', 'r')
lines = f.readlines()
f.close()

target = 0

for line in lines:
    target += int(line)

print(target)
