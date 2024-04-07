col1 = []
col2 = []
fd = open(r"./learn7/input.txt", "r")
text = fd.readlines()
for line in text:
    part = line.split()
    col1.append(part[0])
    col2.append(part[1])

fw = open(r"./learn7/col1.txt", "w")
for line in col1:
    fw.write(line + "\n")
fw = open(r"./learn7/col2.txt", "w")
for line in col2:
    fw.write(line + "\n")