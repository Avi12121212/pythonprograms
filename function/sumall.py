def do_sum(*args):
    total= 0
    for x in args:
        total= total+ x
    return total
    print(total)


print(do_sum(1,2,3,))
