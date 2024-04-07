# 5.6的简单版本
string = "AEIOUaeiou"
word = input("5 words :(space) ")
for x in word.split():
    if x[0] in string:
        print(x, end=" ")