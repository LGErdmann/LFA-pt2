from stack import stack, reset_stack
from states import Q0,Q1,Qf, Qs
from transition import transitions

def automata(fita):
    controle = 0
    global stack
    initial_stack = stack.copy()
    Q0()
    a = True
    while not fita == []:
        result = Q1(fita)
        initial_stack = stack.copy()
        if result == [] and initial_stack == []:
            Qf(result)
            break
        if controle >= 100:
            return print("Fita invalida")
        controle = controle + 1
        if result and result[0] == 'x':
            Qs(result,pilha=initial_stack)
            return 0