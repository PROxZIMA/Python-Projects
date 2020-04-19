# 2, 7, 12, 14, 24, 144, 28, 30, 48, 50, 72, 96, 120, 144
seq = [int(num) for num in (input('Enter the list elements seperated by (, ): ')).split(', ')]
print(seq)
var = [seq[0]]
count = seq[0]
for i in range(len(seq)):
    if seq[i+1]%count == 0:
        count = seq[i+1]
        var.append(seq[i+1])

    print(var)