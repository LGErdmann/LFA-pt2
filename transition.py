from stack import populate, stack, reset_stack
from helpers import separa_elementos
import random







#yuri
#AlfabetoFita=[a,b,c,d,a1,a2,b1,b2,c1,c2,d1,d2,r1,r2,m1,m2,v,f,x]
#AlfabetoPilha=[a,b,c,d,a1,a2,b1,b2,c1,c2,d1,d2,r1,r2,m1,m2,v,f,S,A,B,C,D,A1,A2,B1,B2,C1,C2,D1,D2]
#AlfabetoSaída=[a1,a2,b1,b2,c1,c2,d1,d2,r1,r2,m1,m2,v,f]
#AlfabetGeral=[a,b,c,d,a1,a2,b1,b2,c1,c2,d1,d2,r1,r2,m1,m2,v,f,x,S,A,B,C,D,A1,A2,B1,B2,C1,C2,D1,D2]
def reset_global_variables():
    global stack
    reset_stack() 

def transition_input_tape(input_tape):
    global stack
    if input_tape and stack and stack[-1] == input_tape[0]:
        if input_tape[0] == 'a':
            populate(pop_v='a', push_v='e')
        elif input_tape[0] == 'b':
            populate(pop_v='b', push_v='e')
        elif input_tape[0] == 'c':
            populate(pop_v='c', push_v='e')
        elif input_tape[0] == 'd':
            populate(pop_v='d', push_v='e')
        elif input_tape[0] == 'a1':
            populate(pop_v='a1', push_v='e')
        elif input_tape[0] == 'a2':
            populate(pop_v='a2', push_v='e')
        elif input_tape[0] == 'b1':
            populate(pop_v='b1', push_v='e')
        elif input_tape[0] == 'b2':
            populate(pop_v='b2', push_v='e')
        elif input_tape[0] == 'c1':
            populate(pop_v='c1', push_v='e')
        elif input_tape[0] == 'c2':
            populate(pop_v='c2', push_v='e')
        elif input_tape[0] == 'd1':
            populate(pop_v='d1', push_v='e')
        elif input_tape[0] == 'd2':
            populate(pop_v='d2', push_v='e')
        elif input_tape[0] == 'r1':
            populate(pop_v='r1', push_v='e')
        elif input_tape[0] == 'r2':
            populate(pop_v='r2', push_v='e')
        elif input_tape[0] == 'm1':
            populate(pop_v='m1', push_v='e')
        elif input_tape[0] == 'm2':
            populate(pop_v='m2', push_v='e')
        elif input_tape[0] == 'v':
            populate(pop_v='v', push_v='e')
        elif input_tape[0] == 'f':
            populate(pop_v='f', push_v='e')
        else:
            return False

        input_tape.pop(0)
        return True

    if not stack:
        return 2  # Indicate success when the stack is empty

    return False

def transition_epslon():
    global stack
    if stack[-1] == 'S':
        populate(pop_v='S', push_v='aA')
    elif stack[-1] == 'A':
        populate(pop_v='A', push_v='a1A1')
    elif stack[-1] == 'A1':
        populate(pop_v='A1', push_v='r1m1')
    elif stack[-1] == 'A2':
        populate(pop_v='A2', push_v='r2m2vf')
    elif stack[-1] == 'B':
        populate(pop_v='B', push_v='b1B1')
    elif stack[-1] == 'B1':
        populate(pop_v='B1', push_v='r1m1v')
    elif stack[-1] == 'B2':
        populate(pop_v='B2', push_v='r2m2vf')
    elif stack[-1] == 'C':
        populate(pop_v='C', push_v='c1C1')
    elif stack[-1] == 'C1':
        populate(pop_v='C1', push_v='r2m1')
    elif stack[-1] == 'C2':
        populate(pop_v='C2', push_v='r2m2vf')
    elif stack[-1] == 'D':
        populate(pop_v='D', push_v='d1D1')
    elif stack[-1] == 'D1':
        populate(pop_v='D1', push_v='r1m1vf')
    elif stack[-1] == 'D2':
        populate(pop_v='D2', push_v='r2m2vf')
    else:
        return False

    return True



def transitions(fita):
    global stack
    Defeito = random.randint(1, 99)
    if Defeito < 3:
        fita.append('x')
    while fita:
        if 'x' == fita[0]:
            return fita
        if stack == []:
            reset_global_variables()
            return fita
        Defeito = random.randint(0, 99)

        if not transition_epslon():
            if not fita and stack:
                transition_epslon()
                reset_global_variables()
                return fita
        print(stack)
        if not transition_input_tape(fita):
            reset_global_variables()
            return fita

    return fita