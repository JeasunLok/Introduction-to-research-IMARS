first = eval(input("first number : "))
second = eval(input("second number : "))
operation = input("operation : ")
if operation == "+":
    print("%f %c %f = %f" % (first, operation, second, first+second))
elif operation == "-":
    print("%f %c %f = %f" % (first, operation, second, first-second))
elif operation == "*":
    print("%f %c %f = %f" % (first, operation, second, first*second))
elif operation == "/":
    print("%f %c %f = %f" % (first, operation, second, first/second))
elif operation == "//":
    print("%f %s %f = %f" % (first, operation, second, first//second))
elif operation == "**":
    print("%f %c %f = %f" % (first, operation, second, first**second))
elif operation == "%":
    print("%f %c %f = %f" % (first, operation, second, first%second))
else:
    raise KeyError("the operation input error!")