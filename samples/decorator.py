def decor(func):
    def wrap():
        print("============")
        func()
        print("============")

    return wrap


def decor2(func):
    def wrap():
        print("++++++++++++")
        func()
        print("++++++++++++")

    return wrap


@decor
@decor2
def print_text():
    print("Hello world!")


print_text();