'''
Generadores Logica
'''


def mi_funcion():
    return 4

def mi_generador():
    for x in range(1,5):
        yield 4 
    

'''
print(mi_funcion)
print(mi_generador)

g = mi_generador()

print(next(g))


'''



def mi_segundo_generador():
    x =1 
    yield x
    
    x+=1
    yield x
    
    x+=1
    yield x
    



def mi_tercer_generador():
    num = 7
    count = 1
    
    while True:
        yield num * count
        count +=1




def mensaje():
    x = "Te quedan 3 vidas"
    yield x
    
    x = "Te quedan 2 vidas"
    yield x
 
    x = "Te queda 1 vida"
    yield x
    
    x = "Game Over"
    yield x
 
perder_vida = mensaje()