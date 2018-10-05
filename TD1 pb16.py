def solve(n):
    r=0
    p=10
    while n!=0:
        r+=n%p
        n=(n//p)
    return(r)

assert(solve(2**15)==26)
print(solve(2**1000))
