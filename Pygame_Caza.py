
# Coloca tus importaciones aqui
import pygame
import random
import math
from pygame import mixer

import io


# Inicilizar Pygame
pygame.init()




# Fijar la pantalla titulo, Icono, Fondo 
pantalla_alto, pantalla_ancho = 600, 800
pantalla = pygame.display.set_mode((pantalla_alto, pantalla_ancho))
pygame.display.set_caption('Invacion Lobos')
icono = pygame.image.load("ovejo_lobo.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("background.jpg")


# Cargar fuentes a Byt 
#
fuente_bytes = io.BytesIO(open("Gameplay.ttf", 'rb').read())
fuente = pygame.font.Font(fuente_bytes, 32)

    
    
    
# Cargar sonidos
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.05)
mixer.music.play(-1)
sonido_bala = mixer.Sound("disparo.mp3")
sonido_bala.set_volume(0.3)
sonido_golpe = mixer.Sound("Golpe.mp3")
sonido_golpe.set_volume(0.3)

# Variables del personaje
imagen_personaje = pygame.image.load("minioveja.png")
jugador_x = 268
jugador_y = 736
personaje_velocidad_x = 0
personaje_valocidad_y = 0




# VariablesEnemigo
imagen_lobo = pygame.image.load("lobo.png")
enemigo_x = random.randint(0, 536)
enemigo_y = random.randint(50, 736)
enemigo_velocidad_x = 0.3
enemigo_velocidad_y = 0.3


# Proyectil
imagen_bala = pygame.image.load("bala.png") 
bala_x = 0
bala_y = 700   
bala_velocidad = 3 
bala_y_tasa  = 5
estado_bala = "listo" # --Listo para disparar "fuego" bala en movimiento
puntaje = 0
cartucho = []

# Puntaje
puntaje = 0
text_x = 4
text_y = 10

# Funcion del personaja
def personaje(x,y):
    pantalla.blit(imagen_personaje, (x, y))
    
    
# Funcion Enemigo
def enemigo(x,y,numero_enemigo):
    # Mostrar al enemigo
    try:
        pantalla.blit(imagen_lobo[numero_enemigo], (round(x, 1), y))
    except TypeError :
        print("el enemigo llego a la linea limite")
        
        
# funcionProyectil
def disparar_bala(x,y):
    global estado_bala
    estado_bala = "fuego"
    pantalla.blit(imagen_bala,(x + 16, y + 10 ))


# funcion detectar colicion
def existe_colision(x_objeto1, y_objeto1, x_objeto2, y_objeto2):
    distancia = math.sqrt(math.pow((x_objeto2 - x_objeto1), 2) + (math.pow((y_objeto2 - y_objeto1),2 )))
    return distancia < 27
       

def texto_final():
    fuente_game_over = fuente.render("GAME OVER", True , (255, 255, 255 ))
    pantalla.blit(fuente_game_over,(200,300))
    

# Fuente muestra puntaje acomulado
def mostrar_puntaje(x, y):
    fuente_puntaje_acomulado = fuente.render(f"Puntaje: {puntaje}", True, (255, 150, 0))
    pantalla.blit(fuente_puntaje_acomulado, (x, y))
    
    
def is_atrapada(x_objeto1, y_objeto1, x_objeto2, y_objeto2):
    print(x_objeto1, y_objeto1, x_objeto2, y_objeto2)
    contacto = math.sqrt(math.pow((x_objeto2 - x_objeto1), 2) + (math.pow((y_objeto2 - y_objeto1),2 )))
    return contacto < 32
    

# Variable para varios Enemigos
imagen_lobo = []
enemigo_x = []
enemigo_y = []
enemigo_velocidad_x = []
enemigo_velocidad_y = []
numero_enemigos = 4

for e  in range(numero_enemigos):
    imagen_lobo.append(pygame.image.load("lobo.png"))
    enemigo_x.append(random.randint(0, 536))
    enemigo_y.append(random.randint(50, 200))
    enemigo_velocidad_x.append(0.5)
    enemigo_velocidad_y.append(50)




# Loop del juego
se_ejecuta = True
while se_ejecuta:
    
    
    # RGB patalla
    pantalla.fill((205, 20, 228))
    

    # Imagen fondo
    pantalla.blit(fondo,(0,0))
    
    
    
    # Iterar Evento
    for evento in pygame.event.get():
        
        #EventoCerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False
            
        #EventoPresionar
        if evento.type == pygame.KEYDOWN:
            #print("KEYDOWN")
            
            if evento.key == pygame.K_LEFT:
                # print("Presionó la tecla izquierda")
                personaje_velocidad_x = -1
            if evento.key == pygame.K_RIGHT:
                # print("Presionó la tecla derecha")
                personaje_velocidad_x = +1
            if evento.key == pygame.K_DOWN:
                # print("Presionó la tecla hacia abajo")
                personaje_valocidad_y = +1
            if evento.key == pygame.K_UP:
                # print("Presionó la tecla hacia arriba")
                personaje_valocidad_y = -1
            if evento.key == pygame.K_SPACE and estado_bala == "listo":
                bala_x = jugador_x
                
                bala_y -= bala_velocidad 
                sonido_bala.play()
                disparar_bala(bala_x, bala_y)
                '''
                                          nueva_bala = {
                        "x": jugador_x,
                        "y": jugador_y,
                        "velocidad": -5
                    }
                    
                    
                    cartucho.append(nueva_bala)
                    bala_x = jugador_x
                    bala_y = jugador_y
                    disparar_bala(bala_x, bala_y)
                      
     
                 '''                  
        # Evento soltar  
        if evento.type == pygame.KEYUP:
            if evento.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                
                # Parar el movimiento 
                personaje_valocidad_y = 0
                personaje_velocidad_x = 0

    # Modificar Ubicacion de la Oveja          
    jugador_x += personaje_velocidad_x
    jugador_y += personaje_valocidad_y
    
    # Limitar bordes jugador
    if jugador_x <=0:
        jugador_x = 0   
    elif jugador_x >= pantalla_alto - 64:
        jugador_x = pantalla_alto - 64  
    if jugador_y <= 5:
        jugador_y = 5
    elif jugador_y >= pantalla_ancho - 64 :
        jugador_y = pantalla_ancho - 64
                   
    # LimitadorBordes del lobo
    if enemigo_x[e] <= 0:
        enemigo_velocidad_x[e] = 0.3
    elif enemigo_x[e] >= 536:
        enemigo_velocidad_x[e] = -0.3 
    if enemigo_y[e] <= 1:
        enemigo_velocidad_y[e] = 0.3
    elif enemigo_y[e] >= 736:
        enemigo_velocidad_y[e] = -0.3            
        
    # Movimientos y colision del enemigo
    for e in  range(numero_enemigos): 
        enemigo_x[e] += enemigo_velocidad_x[e]
        if enemigo_x[e] <= 0 or enemigo_x[e] >= pantalla_alto - 64 :
            enemigo_velocidad_x[e] = - enemigo_velocidad_x[e]
            enemigo_y[e] += enemigo_velocidad_y[e]
        if enemigo_y[e] <= 0 or enemigo_y[e] >= pantalla_ancho -64:
            enemigo_velocidad_y[e] = - enemigo_velocidad_y[e]
            enemigo_y[e] += enemigo_y[e]
        
        # Colision
        colision = existe_colision(enemigo_x[e],enemigo_y[e], bala_x, bala_y)
        #print(colision)
        if colision:
            bala_y = 700
            estado_bala = "listo"                         
            puntaje += 1
            sonido_golpe.play()
            enemigo_x[e] = random.randint(0, pantalla_alto - 64)
            enemigo_y[e] = random.randint(50, int(pantalla_ancho / 2) )  
            # print(enemigo_x[e], '--- ', enemigo_y[e])
             
        enemigo(enemigo_x[e], enemigo_y[e], e)
            
        # Juego terminado
        cachado =  is_atrapada(jugador_x, jugador_y, enemigo_x[e], enemigo_y[e])
        if cachado:
            print("atrapada")
            
            for k in range(numero_enemigos):
                enemigo_y[k] = 1000
                texto_final()
                pass
                


        
    # Movimeinto Proyectil
    

    if estado_bala == "fuego":
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_velocidad   
         
        if bala_y <= 0:
            bala_y = 700
            estado_bala = "listo"
            
        
    # Funciones
    personaje(jugador_x, jugador_y)
    mostrar_puntaje(text_x,text_y)
    
    #Actualizar    
    pygame.display.update()
                
                
            










