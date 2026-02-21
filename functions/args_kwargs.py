def total(*args):
    return sum(args)

print(total(1, 2, 3))

def info(**kwargs):
    print(kwargs)

info(name="Yerkosh", age=18)