def min(x, y):
    result = (lambda: y, lambda: x)[x < y]()
    return result


def max(values_list):
    max = values_list[0]
    for elem in values_list:
        if(elem > max):
            max = elem
    return max 


def len(values_list):
    counter = 0
    for i in values_list:
        counter = counter + 1
        return counter


def multiply(x, y):
    return x*y


def pow(x, y):
    return x**y


def divmod(x, y):
    return x//y


if __name__ == "__main__":
    print(min(1, 2))
    print(max([9, 4, 6]))
    print(len(['a', 'b', 'v']))
    print(multiply(2, 3))
    print(pow(2, 3))
    print(divmod(4, 2))


