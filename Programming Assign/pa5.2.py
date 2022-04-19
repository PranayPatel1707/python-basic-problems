try:
    a = [1,2,3]
    print(a[4])
except LookupError:
    print("Index out of bounds error")