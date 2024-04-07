# 打印首字母为原因的输入单词 
string = "aeiouAEIOU"
a_list = []
for i in range(5):
    word = input("a word : ")
    a_list.append(word)
print(a_list)
print("result : ")
for i in range(5):
    for ch in string:
        if a_list[i][0] == ch:
            print(a_list[i])
            break