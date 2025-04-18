def display_multiplication_table(n, i):
    print(f"{n} x {i} = {n * i:2d}", end='\t')

for i in range(1, 10):
    for n in range(2, 6):
        display_multiplication_table(n, i)
    print()
print() 

for i in range(1, 10):
    for n in range(6, 10):
        display_multiplication_table(n, i)
    print()
