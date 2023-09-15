# *args & ** kwargs


def adder(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print("sum:" ,sum)

adder (5,6)