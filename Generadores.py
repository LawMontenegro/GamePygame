'''
Generadores 'yield'

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
    
    

def mi_generador():
    num = 1
    while True:
        yield num
        num += 1
        
'''
generador = mi_generador()
print(next(generador))
print(next(generador))  
'''  



def mi_generador():
    num = 7
    count = 1
    
    while True:
        yield num * count
        count +=1
        
        
        
'''
generador = mi_generador()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

        '''
        
def mi_generado():
    vidas =  3
    while vidas != 0:
        yield f"Te quedan {vidas} vidas"
        vidas -=1
    if vidas == 1 :
        yield "Te queda 1 vida"
    if vidas == 0:
        yield "Game Over"

    
    
perder_vida = mi_generado()  

print(next(perder_vida))
print(next(perder_vida)) 
print(next(perder_vida)) 
print(next(perder_vida))       


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