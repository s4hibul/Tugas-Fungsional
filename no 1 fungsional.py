lst = [1,2,3,4]
def sum_squares(x):
    return x*x
total = list(map(sum_squares,lst))
print(sum(total))