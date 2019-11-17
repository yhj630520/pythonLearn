def double(arg):
    print("Before: ", arg)
    arg = arg * 2
    print("After: ", arg)


def change(arg):
    print("Before: ", arg)
    arg.append('More data')
    print("After: ", arg)


double(10)
double('Hello ')
double([1, 2, 3, 4])

change([1, 2, 3, 4])
