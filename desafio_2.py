def pertence_fibonacci(numero):
    primeiro, segundo = 0, 1
    while segundo <= numero:
        if segundo == numero:
            return True
        primeiro, segundo = segundo, primeiro + segundo
    return False


n = int(input('Digite um número para saber se ele pertence a sequência de Fibonacci: '))
if pertence_fibonacci(n):
    print(f'O valor {n} esta presente na sequência!')
else:
    print(f'O valor {n} não esta presente na sequência')
