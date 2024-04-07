ch = input("ch : ")
if "a" <= ch <= "z" or "A" <= ch <= "Z":
    print("%c is character" % ch)
elif "0" <= ch <= "9":
    print("%c is number")
else:
    print("%c is symbol")