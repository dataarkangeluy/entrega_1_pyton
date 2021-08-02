#####  Gabriel Caceres, curso de Pyhton 1 - 2021
#####  
##### - para las imagenes ascii utilice arte ASCII de fuentes publicas como     https://fsymbols.com/es/arte-de-texto #################
##### - para  darle color a los textos en consola, utilice esta referencia....  https://python-para-impacientes.blogspot.com/2016/09/dar-color-las-salidas-en-la-consola.html  #################
#####  


################# Bibliotecas Necesarias ##############
# !pip install unidecode  # Instala sistema de codificación de caracteres para levantar archivo
import time
import random 

#################  LEO ARCHIVO con peliculas y limpio de caracteres raros con encoding #################
with open('Presentacion_tarea\pelis.txt', encoding="utf-8") as f:
    mis_peliculas = f.readlines()
f.close() 

mis_peliculas_limpias = []   # inicializo lista
for pelicula in mis_peliculas:
    mis_peliculas_limpias.append(pelicula.strip())  # voy agregando una a una y limpio espacios en blancos al inicio y final de cada elemento

# print(mis_peliculas_limpias)
##################################################################################################################################



##############  Utilizo funcion para dibujar la calicatura del ahorcado cada vez que exista un error  #############################
def errores(v):
    if v == 5:
        print("\033[2J\033[1;1f") # Borrar pantalla y situa cursor
        print(""" ERROR, ahora tienes la cabeza..!
                ...
                ... ----- +
                ... |     |
                ... |  \033[1;31m   O   \033[0;m
                ... |    
                ... |      
                ... |    
                ... ============
                                                """)
    if v == 4:
        print("\033[2J\033[1;1f") # Borrar pantalla y situa cursor
        print(""" ERROR, ahora tienes la cabeza, y el tronco..!
                ...
                ... ----- +
                ... |     |
                ... |  \033[1;31m   O   \033[0;m  
                ... |  \033[1;31m   |   \033[0;m
                ... |  \033[1;31m   |   \033[0;m  
                ... |      
                ... ============
                                                """)
    if v == 3:
        print("\033[2J\033[1;1f") # Borrar pantalla y situa cursor
        print(""" ERROR, ahora tienes cabeza, tronco y 1 pierna..!
                ...
                ... ----- +
                ... |     |
                ... |  \033[1;31m   O   \033[0;m
                ... |  \033[1;31m   |   \033[0;m
                ... |  \033[1;31m   |   \033[0;m  
                ... | \033[1;31m   /   \033[0;m 
                ... ============
                                                """)


    if v == 2:
        print("\033[2J\033[1;1f") # Borrar pantalla y situa cursor
        print(""" ERROR, ahora tienes cabeza, tronco y 2 pierna..!
                ...
                ... ----- +
                ... |     |
                ... |  \033[1;31m   O   \033[0;m  
                ... |  \033[1;31m   |   \033[0;m
                ... |  \033[1;31m   |   \033[0;m  
                ... | \033[1;31m   / \\   \033[0;m
                ... ============
                                                """)   



    if v == 1:
        print("\033[2J\033[1;1f") # Borrar pantalla y situa cursor
        print(""" ERROR, ahora YA tienes hasta 1 brazo (te queda una sola chance)..!!
                ...
                ... ----- +
                ... |     |
                ... |  \033[1;31m   O   \033[0;m  
                ... | \033[1;31m   /|   \033[0;m
                ... |  \033[1;31m   |   \033[0;m  
                ... | \033[1;31m   / \\   \033[0;m
                ... ============
                                                """)                                                      
    if v == 0:
        print("\033[2J\033[1;1f") # Borrar pantalla y situa cursor
        print(""" \033[1;31m   GAME OVER, no tienes mas vidas..!
                ...
                ... \033[1;31m   ----- +   \033[0;m
                ... \033[1;31m   |     |   \033[0;m
                ... \033[1;31m   |     O   \033[0;m   
                ... \033[1;31m   |    /|\\   \033[0;m
                ... \033[1;31m   |     |   \033[0;m  
                ... \033[1;31m   |    / \\   \033[0;m
                ... \033[1;31m   ============   \033[0;m
                                                """)




###################################################  BIENVENIDA  #################################################################

print("\033[2J\033[1;1f") # Borro la consola 
print(""" \033[1;33m
                                 \|||/
                                 (o o)
                        ------ooO-(_)-Ooo------
                        EL JUEGO DEL AHORCADO \033[0;m
\033[1;35m
INSTRUCCIONES:\033[0;m El Objetivo del juego es descubrir el nombre de la pelicula secreta.
Al iniciar el juego podras pedir una letra o adivinar la pelicula.
Si la letra no está en el nombre de la pelicula, entonces perderas una vida....
Obtienes la victoria si logras \033[1;35madivinar\033[0;m la pelicula secreata, \033[1;35mantes de gastar tus 6 vidas.\033[0;m 
     """)



################# Conecto con el jugador, para obtener un juego mas simpatico. #####################################################################

nombre=input("\033[1;32m Como te llamas?\033[0;m ")
time.sleep(3)
print("\033[2J\033[1;1f") # Borrar pantalla y situa cursor 
print("Hola \033[1;33m" + nombre + "\033[0;m, es hora de jugar !!")

 



################# PELICULA RANDOM - eligo la pelicula al azar,  y la muestro en pantalla al participante ################################################
def selectRandom(mis_peliculas_limpias):
    return random.choice(mis_peliculas_limpias)
pelicula_random = selectRandom(mis_peliculas_limpias)
pelicula_minuscula = [x.lower() for x in pelicula_random]  #convierto a minuculas la pelicula secreta

time.sleep(1)
print(" ")
print(f"La pelicula secreta es: \033[1;31;47m {pelicula_random} \033[0;m ")
print(f"""
Estas es la cantidad de letras que tien tu pelicula secreta, es la hora de adivinar su nombre....!!
""")





################################################### COMIENZA EL JUEGO  ##################################################################################

#################  inicializo variables 
tus_letras=" "
vidas=6

############### # El juego continua, mientras se tengan vida (vidas > 0) o el jugador adivine la pelicula_minuscula (saliendo del while con break)
while vidas > 0: # Controlo el numero de vidas
    fallas=0     # inicializo variable de fallas ante el no acierto de letras
    print(f"{fallas} fallas1")    

    ##################################################################################
    ### con la instruccion FOR recorro letra a letra y voy verificando con if si la letra tien acierto o no, en caso de NO acertar, resto 1 vida  ######    
    for letra in pelicula_minuscula:
         
        if letra in tus_letras:     # verifico si la letra esta en la pelicula
            
            print("\033[1;35m" +  letra + "\033[0;m", end="")     # si está la imprimo 
        else:                        
            
            print("_",end="")  # si no esta, oculo letras y sumo una vida al contador       
            fallas+=1   
            
        
     ##################################################################################
     # verifico si al salir del FOR, las fallas = 0 el participante gano y corto el ciclo while
    print(f"{fallas} fallas3")      
    if fallas==0:  # 
        print("""
                
    |@@@@|     |####|
    |@@@@|     |####|
    |@@@@|     |####|
    \@@@@|     |####/
     \@@@|     |###/
      `@@|_____|##'
           (O)
        .-'''''-.
      .'  * * *  `.
     :  *       *  :
    :  Felicidades  :
    : ~ \033[1;34mGANASTE ! \033[0;m~ :
     :  *       *  :
      `.  * * *  .'
        `-.....-'   
        
 La pelicula secreta era \033[1;35m""" +  pelicula_random + """\033[0;m
 
 """)
        ########################### Arte de texto ascii copiada de https://fsymbols.com/es/arte-de-texto/#all_cats   #################################                  
                       
        break  # corto con el ciclo while
        



    ############################## INGRESO Y CONTROLO ACIERTOS Y ERRORES ####################################################  
    
    tuletra=input("""
    
Introduce una letra: """).lower() # paso el input a minusculas
    
    if tuletra == " ":   # controlo que no ingrese un espacio
        print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
        errores(vidas)
        print("\033[1;31m" + "ERROR: No se permite ingresar espacio" + "\033[0;m")
    else:
        if len(tuletra) != 1:   # controlo que solo se ingrese un caracter        
            print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
            print("\033[1;31m" + "ERROR: Solo esta permitido ingresar 1 letra o numero" + "\033[0;m")
        else:
            tus_letras+=tuletra 
            if tuletra not in pelicula_minuscula:
                vidas-=1
                errores(vidas)
                print("""
                            Letra no encontrada, ahora te quedan """ + "\033[1;31m" + f"{vidas}" + "\033[0;m" + " vidas.")

                print("Historial de letras ingresadas: " + "\033[1;31m" +  tus_letras + "\033[0;m") # muestro la lista de letras ingresadas
                   
                if vidas== 0:          
                    print("\033[1;31m" + """
██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████  
██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██ 
██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████  
██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ 
██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██ 
                                                                           """ + "\033[0;m")
                ########################### Arte de texto ascii generada en https://patorjk.com/software/taag/#p=display&f=ANSI%20Regular&t=Game%20Over    #################################




    
else:  # el else de while que se ejecuta una vez que la condición sea falsa, o sea cuando termina el juego sin usar el break
    print(""" 
La pelicula secreta era \033[1;35m""" +  pelicula_random + """\033[0;m  
             \033[1;33m\|||/\033[0;m
             (\033[1;34mo o\033[0;m)
    ------ooO-(_)-Ooo------   
╔════════════════════════════╗ 
║   Gracias por Jugar! \033[1;31m♥♥♥\033[0;m   ║ 
╚════════════════════════════╝ 
    --------------------
           \033[1;35m|__|__|\033[0;m 
            || || 
           ooO Ooo              """)   
    ########################### Arte de texto ascii generada en https://norfipc.com/facebook/dibujos-figuras-ascii-firmar-pegar-muro-facebook.html   #################################                                     

            