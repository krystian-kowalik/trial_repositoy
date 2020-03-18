def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))


say_hi("Mike", 35)
say_hi("Steve", 14)


def mnozenie(a=[]):
    for x in range(len(a)):
        a[x] += pow(x, 6)


x = [4, 6, 7, 8]
mnozenie(x)
print(x)

