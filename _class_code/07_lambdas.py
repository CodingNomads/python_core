# DON'T DO THIS (assigning a lambda expression to a variable)
# squ = lambda x: x**2


def square(x):
    return x**2

print(square(2))


list_ = [1, 2, 3]

# you can use lambda functions as "throwaway" functions - something
# that you use only once and then discard, e.g.:
res_lam = list(map(lambda x: x**2, list_))
res_fun = list(map(square, list_))  # same thing can be done with a named func
print(res_lam)
print(res_fun)

# you can also reproduce lambda's functionality with a list comprehension
# res_lam = list(map(lambda x: x**2, list_))  # is the same as:
res = list(x**2 for x in list_)
print(res)
