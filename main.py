from helpers import separa_elementos
from states import Q0,Q1
from stack import stack, reset_stack
import streamlit
from pushdown_automata import automata


#"aa1r1m1"
def main(cont, fita):
    while True:
        while cont >= 0:
            automata(fita)
            cont = cont - 1
        return 0

def escolha_carro():
    print("\n# Coódigos de montagem #\n")
    print("Modelo A\n A1 - aa1r1m1\n A2 - aa2r2m2vf")
    print("\nModelo B\n B1 - bb1r1m1v\n B2 - bb2r2m2vf")
    print("\nModelo C\n C1 - cc1r2m1\n C2 - cc2e2m2vf")
    print("\nModelo D\n D1 - dd1r1m1vf\n D2 - dd2r2m2vf")
    fita = input("\nCódigo do carro: ")
    cont = input("\nQuantidade de carros a serem montadas: ")

    return fita , cont

fita, cont = escolha_carro()
fita = separa_elementos(fita)


main(cont=int(cont), fita=fita)