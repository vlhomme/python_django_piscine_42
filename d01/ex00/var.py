def okBoomer(val):
    print("{} est de type {}".format(val, type(val)))

def my_var():
    okBoomer(42)
    okBoomer("42")
    okBoomer("quarante-deux")
    okBoomer(42.0)
    okBoomer(True)
    okBoomer([42])
    okBoomer({42: 42})
    okBoomer((42,))
    okBoomer(set())

if __name__ == '__main__':
    my_var()
