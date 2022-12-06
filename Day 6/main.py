file = "input.txt"
packets = open(file).read().strip()

for i in range(len(packets)):
    signal = packets[i:i+14]
    if len(set(signal)) == 14:
        print(i + 14)
        break