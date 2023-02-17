def soma_10(i):
    print(f'Dentro - O valor de i antes {i}')
    i += 10
    print(f'Dentro - O valor de i depois {i}')


i = 20
print(f'Fora - O valor de i antes {i}')
soma_10(i)
print(f'Fora - O valor de i depois {i}')
