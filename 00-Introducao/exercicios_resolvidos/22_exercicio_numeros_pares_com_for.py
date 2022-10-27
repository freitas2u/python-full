#Exiba todos os números pares entre 1 e 1000 usando o for

#Forma 1
for i in range(1, 1001):
    if i % 2 == 0:
        print(i)

#Forma 2
for i in range(2, 1001, 2):
    print(f"Forma 2: {i}")
