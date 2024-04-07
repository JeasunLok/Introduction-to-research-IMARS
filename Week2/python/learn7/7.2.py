f = open(r"./learn7/number.txt", "r")
number_list = f.read()
print(number_list)
number_list = list(eval(number_list))
print(number_list)
number_list.sort()
print(number_list)

f = open(r"./learn7/number_sort.txt", "w")
for number in number_list:
    f.write(str(number) + " ")