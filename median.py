lst = [1, 5, 7, 16, 2, 4, 3, 77]
lst.sort()

n = len(lst)
if n % 2 == 1:

    median_value = lst[n // 2]
else:
   
    median_value = (lst[n // 2 - 1] + lst[n // 2]) / 2

print(median_value)
