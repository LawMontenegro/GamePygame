'''

decoradores
'''


def cambiar_letras(tipo):
    def mayuscula(texto):
        return texto.upper()
    
    def minuculas(texto):
        return texto.lower()
    
    if tipo == 'may':
        return mayuscula
    elif tipo == 'min':
        return minuculas
    
'''
operacion = cambiar_letras('min')
operacion("palabra")
print(operacion)
print(operacion("palabra"))    


'''


def decorar_saludo(funcion):
    def otra_fincion(palabra):
        print("holaa")
        funcion(palabra)
        print("adios")
        
    return otra_fincion

#@decorar_saludo
def mayusculaOtroEjemplo(texto):
    print (texto.upper())
    
#@decorar_saludo
def minuculasOtroEjemplo(texto):
    print (texto.lower())

mayucula_decorada = decorar_saludo(mayusculaOtroEjemplo)
minuscula_decorada = decorar_saludo(minuculasOtroEjemplo)

mayucula_decorada("hola que tal aprendiento como envolver funciones")


minuscula_decorada("Python esta en MUYUSCULAS ")

minuculasOtroEjemplo("bye bye")