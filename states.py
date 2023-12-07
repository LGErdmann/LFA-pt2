from stack import populate, reset_stack,stack
from helpers import separa_elementos
from transition import transitions,reset_global_variables



def Q0():
    global stack
    return populate(push_v="S")

def Q1(fita):
    global stack
    Q0()
    fita = separa_elementos(fita)
    fita = transitions(fita)

        
    
    

            
            
    return fita

def Qf(fita):
    global stack
    reset_global_variables()
    print(stack)
    print("Montagem com exito\n")
    return 0

def Qs(fita,pilha):
    print("\nErro: peça defeituosa, segue onde foi o erro de proceeso de montagem")
    print(pilha) # estado da pilha quando deu erro
    pilha = []
    return 0







 



