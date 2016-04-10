import os
import time

def animation(NAME,SECUENCE,times,seconds):
    """Using the animation function with the name of a vector of ASCII draws,the secuence,number of repetitions and time for each image:
    [animation(NAME,SECUENCE,times,seconds)], executesthe animation in a terminal.
    
    A partir del nombre de un vector de cadenas en forma de imágenes, la secuncia de estas, el numero de repeticiones y el tiempo para
    cada imagen: [animation(NAME,SECUENCE,times,seconds)], ejecuta la animación en un terminal."""

    for i in range(times):
        for i in range(len(SECUENCE)):
            os.system("cls")
            print(NAME[SECUENCE[i]-1])
            time.sleep(seconds)
