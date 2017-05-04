def F(n):
    if n == 0 or n == 1:
        return 1
    return F(n-1)+F(n-2)
print(F(100))