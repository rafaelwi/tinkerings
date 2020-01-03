# PyPlaysPokemon
#   A quick script by github.com/rafaelwi

import pyautogui as pag
import time as t
import random

# Wait for setup
for i in range(5, -1, -1):
    print('Starting script in ', i, 'seconds...')
    t.sleep(1)

print("Starting script")

# Randomly press buttons
while(True):
    # Choose a number from 1-8
    p = random.randint(1,12)

    if p <= 2:
        pag.keyDown('up')
        t.sleep(1/60)
        pag.keyUp('up')
        print('Pressed up!')
    elif p <= 4:
        pag.keyDown('down')
        t.sleep(1/60)
        pag.keyUp('down')
        print('Pressed down!')
    elif p <= 6:
        pag.keyDown('left')
        t.sleep(1/60)
        pag.keyUp('left')
        print('Pressed left!')        
    elif p <= 8:
        pag.keyDown('right')
        t.sleep(1/60)
        pag.keyUp('right')
        print('Pressed right!')
    elif p == 9:
        pag.keyDown('x')
        t.sleep(1/60)
        pag.keyUp('x')
        print('Pressed B!')
    elif p == 10:
        pag.keyDown('z')
        t.sleep(1/60)
        pag.keyUp('z')
        print('Pressed A!')
    elif p == 11:
        pag.keyDown('enter')
        t.sleep(1/60)
        pag.keyUp('enter')
        print('Pressed START!')
    elif p == 12:
        pag.keyDown('backspace')
        t.sleep(1/60)
        pag.keyUp('backspace')
        print('Pressed SELECT!')

    t.sleep(0.16)