
Symbols = ['a', 'b', 'c', 'd', 'a1', 'a2', 'b1', 'b2', 'c1', 'c2', 'd1', 'd2', 'r1', 'r2', 'm1', 'm2', 'v', 'f', 'x', 'S', 'A', 'B', 'C', 'D', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2']

def separa_elementos(fita, Symbols=Symbols):
    elementos = []
    while len(fita) > 0:
        elemento = fita[0]
        elementos.append(elemento)
        fita = fita[1:]
        new_elementos = arruma_symbols(elementos, Symbols)
    return new_elementos



def arruma_symbols(elementos, Symbols=Symbols):
    new_elementos = []
    jit = False

    for x in range(len(elementos)):
        if jit:
            jit = False
            continue

        if x + 1 >= len(elementos):
            new_elementos.append(elementos[x])
            return new_elementos

        a = elementos[x] + elementos[x+1]
        if a in Symbols:
            new_elementos.append(a)
            jit = True
        else:
            new_elementos.append(elementos[x])

    return new_elementos
