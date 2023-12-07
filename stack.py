from helpers import separa_elementos
global stack
stack = []
def populate(pop_v="e", push_v="e"):
    Symbols = ['a', 'b', 'c', 'd', 'a1', 'a2', 'b1', 'b2', 'c1', 'c2', 'd1', 'd2', 'r1', 'r2', 'm1', 'm2', 'v', 'f', 'x', 'S', 'A', 'B', 'C', 'D', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2']

   
    if pop_v != "e":
        pop_v = separa_elementos(pop_v, Symbols)
        for x in pop_v:
            while stack and stack[-1] == x:
                stack.pop()


    if push_v != "e":
        push_v = separa_elementos(push_v, Symbols)
        stack.extend(reversed(push_v))

    return None

def reset_stack():
    global stack
    stack.clear()

