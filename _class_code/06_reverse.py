# nope
list_ = [1, 2, 3, 4, 5, ]
for i in range(len(list_)):
    list_[i] = list_[len(list_) - 1 - i]

print(list_)

# same nope
list_ = [1, 2, 3, 4, 5, ]
store = 0
for i in range(len(list_) // 2):
    store = list_[i]
    list_[i] = list_[len(list_) - 1 - i]

print(list_)

# yep works!
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
store = 0
for i in range(len(list_) // 2):
    store = list_[i]
    list_[i] = list_[len(list_) - 1 - i]
    list_[len(list_) - 1 - i] = store

print(list_)
