offset = 1000
ports = [1072, 1101, 1108, 1108, 1111]

for p in ports:
    print(chr(p - offset), end="")
