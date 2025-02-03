lis = [1,2,3,4,5,6]

result = filter(lambda n : n % 2 == 0, lis)
result2 = map(lambda x : x * 2, lis)
print(list(result))
print(list(result2))