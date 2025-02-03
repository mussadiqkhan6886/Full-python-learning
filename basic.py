def recurse(n, a):
    if n == 0:
        print(a)
    else:
        recurse(n-1, n+a)
        
recurse(2,0)