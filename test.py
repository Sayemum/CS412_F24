def recurse(n, target, my_list):
    if n <= 0:
        return False
    if n == target:
        return True
    
    my_list.append(n)
    return recurse(n - 1, target, my_list)

my_list = []
print(recurse(10, 5, my_list))
print(my_list)