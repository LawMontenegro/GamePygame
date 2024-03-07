import pygame
import random
import math
from pygame import mixer

#Inicilizar Pygame
pygame.init()

#Crear la pantalla
pantalla = pygame.display.set_mode((600,800))

#Titulo, Icono, Fondo 
pygame.display.set_caption('Invocacion de Oveja')
icono = pygame.image.load("aceite-de-oliva.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("28512.jpg")

'''#musicoFondo
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.1)
mixer.music.play(-1)
 '''

#Variables de personaje
imagen_oveja = pygame.image.load("minioveja.png")
oveja_x = 268
oveja_y = 736
oveja_x_cambio = 0
oveja_y_cambio = 0


#FuncionOveja
def oveja(x,y):
    pantalla.blit(imagen_oveja, (x, y))


#puntaje
puntaje = 0
fuente = pygame.font.Font("Gameplay.ttf", 32)
text_x = 4
text_y = 10
 
#textoGameOver

fuente_final = pygame.font.Font("Gameplay.ttf", 40)
def texto_final():
    fuente_game_over = fuente_final.render("JUEGO TERMINADO", True , (255, 255, 255 ))
    pantalla.blit(fuente_game_over,(60,200))
    
     
    
    
    
    
    
    
    
    pass

#funcionMostrarPuntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 0, 0))
    pantalla.blit(texto, (x, y))


    
    
#variableProyectil
imagen_bala = pygame.image.load("bala.png") 
bala_x = 0
bala_y = 700
bala_x_tasa = 0
bala_y_tasa  = 5
bala_visible = False
puntaje = 0
balas = []


# funcionProyectil
def bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(imagen_bala,(x + 16, y +10 ))
    
#funcion detectar colicion
def existe_colision(x_objeto1, y_objeto1, x_objeto2, y_objeto2):
    distancia = math.sqrt(math.pow((x_objeto2 - x_objeto1), 2) + (math.pow((y_objeto2 - y_objeto1),2 )))
    
    if distancia < 40 :
        print(f"murio a {distancia} distancia")
        return True
    else:
        return False
       
        
    

 



#VariablesEnemigo
imagen_lobo = pygame.image.load("lobo.png")
lobo_x = random.randint(0, 536)
lobo_y = random.randint(50, 736)
lobo_x_tasa_cambio = 0.3
lobo_y_tasa_cambio = 0.3




#variableParavariosEnemigos
imagen_lobo = []
lobo_x = []
lobo_y = []
lobo_x_tasa_cambio = []
lobo_y_tasa_cambio = []
cantidad_lobo = 4

for e  in range(cantidad_lobo):
    imagen_lobo.append(pygame.image.load("lobo.png"))
    lobo_x.append(random.randint(0,536))
    lobo_y.append(random.randint(50,200))
    lobo_x_tasa_cambio.append(0.5)
    lobo_y_tasa_cambio.append(50)


#FuncionEnemigo
def lobo(x,y,numero_enemigo):
    #lanza al lobo en
    pantalla.blit(imagen_lobo[numero_enemigo], (x, y))


#Loop del juego
se_ejecuta = True
while se_ejecuta:
    
    
    # RGB patalla
    pantalla.fill((205, 250, 228))
    

    #Imagen fondo
    pantalla.blit(fondo,(0,0))
    
    
    
    #Iterar Evento
    for evento in pygame.event.get():
        
        #EventoCerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False
            
        #EventoPresionar
        if evento.type == pygame.KEYDOWN:
            #print("KEYDOWN")
            
            if evento.key == pygame.K_LEFT:
                print("Presionó la tecla izquierda")
                oveja_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                print("Presionó la tecla derecha")
                oveja_x_cambio = +1
            if evento.key == pygame.K_DOWN:
                print("Presionó la tecla hacia abajo")
                oveja_y_cambio = +1
            if evento.key == pygame.K_UP:
                print("Presionó la tecla hacia arriba")
                oveja_y_cambio = -1
            if evento.key == pygame.K_SPACE:
              
                if not bala_visible:
                    sonido_bala = mixer.Sound("disparo.mp3")
                    sonido_bala.set_volume(0.3)
                    sonido_bala.play()
                    nueva_bala = {
                    "x": oveja_x,
                    "y": oveja_y,
                    "velocidad": -5
                    }
                    balas.append(nueva_bala)
                    print(balas)
                    
                    print("espacio")
                    bala_x = oveja_x
                    bala_y = oveja_y
                    bala(bala_x, bala_y)
                
                
        #EventoSoltar  
        if evento.type == pygame.KEYUP:
            if evento.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                print("Soltó una tecla")
                #Parar el movimiento 
                oveja_y_cambio = 0
                oveja_x_cambio = 0
                
    #Modificar Ubicacion de la Oveja         
    oveja_x += oveja_x_cambio
    oveja_y += oveja_y_cambio
    
    #LimitadorBordes a la oveja
    if oveja_x <=0:
        oveja_x = 0
    elif oveja_x >= 536:
        oveja_x = 536
        
    if oveja_y <= 5:
        oveja_y = 5
    elif oveja_y >= 736:
        oveja_y = 736
        
        
    #Modificar Ubicacion del lobo  
    for e in  range(cantidad_lobo):    
        
          
        #fin del juego
        if lobo_y[e] >250:
            for k in range(cantidad_lobo):
                lobo_y[k] = 1000
                texto_final()
                break
                
                
        
        
        lobo_x[e] += lobo_x_tasa_cambio[e]
        lobo_y[e] += lobo_y_tasa_cambio[e]
    
    
        #LimitadorBordes del lobo
        if lobo_x[e] <= 0:
            lobo_x_tasa_cambio[e] = 0.3
        elif lobo_x[e] >= 536:
            lobo_x_tasa_cambio[e] = -0.3
            
        if lobo_y[e] <= 1:
            lobo_y_tasa_cambio[e] = 0.3
            
        elif lobo_y[e] >= 736:
            lobo_y_tasa_cambio[e] = -0.3
            
            
            
            
            
        #Verifica Colicion
    for bala in balas:
        
        colision_bala_lobo = existe_colision(lobo_x[e], lobo_y[e], bala["x"], bala["y"])
        
                        #sonido de golpe
        golpe = mixer.Sound("Golpe.mp3")
        golpe.set_volume(0.3)
        golpe.play()
        balas.remove(bala)
        
        #Suma puntaje
        puntaje += 1
        
        #reinicia ubicacion dek lobo
        lobo_x[e] = random.randint(0,300)
        lobo_y[e] = random.randint(20,736)
        break

    lobo(lobo_x[e], lobo_y[e], e)
        
    #movimeintoProyectil
    if bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(imagen_bala, (bala["x"] + 16, bala["y"] + 10 ))
        if bala["y"] < 0:
            balas.remove(bala)
        
        
    #limitacion de bordes proyetil
    if bala_visible:
        bala(bala_x, bala_y)
        bala_y -= bala_y_tasa
        
    
    

    
    
    
    
    #funciones
    oveja(oveja_x, oveja_y)
    
    mostrar_puntaje(text_x,text_y)
    
    
    
    #Actualizar    
    pygame.display.update()
                
                
            










