import time
import random
from matcheo import matcheo
opciones = {
    'piedra':{'tijera': "Piedra aplasta a Tijeras", 'lagarto': 'Piedra aplasta a Lagarto'},
    'papel': {'piedra': "Papel cubre a Piedra", 'spock': "Papel refuta a Spock"},
    'tijera': {'papel': "Tijeras cortan a Papel", 'lagarto': "Tijeras decapitan a Lagarto"},
    'spock': {'tijera': "Spock destroza a Tijeras", 'piedra': "Spock vaporiza a Piedra"},
    'lagarto': {'papel': "Lagarto come a Papel", 'spock': "Lagarto envenena a Spock"}
}
print("¡Bienvenido al juego de Piedra, Papel, Tijera, Lagarto o Spock!")
time.sleep(1)
jugador = input("¿Cuál es tu nombre? ")
print(f"Hola, {jugador.capitalize()}! Vamos a jugar.")
time.sleep(1)
print("¿Sabes las reglas?")
reglas = input("Escribe 'sí' o 'no': ").lower()
if reglas == 'no':
    print("Las reglas son las siguientes:")
    time.sleep(1)
    print("Juegas tu contra la CPU y cada uno elige una de las siguientes opciones:")   
    print("1. 'Piedra' que aplasta a Tijeras y Lagarto.")
    print("2. 'Papel' cubre a Piedra y refuta a Spock.")
    print("3. 'Tijeras' cortan a Papel y decapitan a Lagarto.")
    print("4. 'Spock' destroza a Tijeras y vaporiza a Piedra.")
    print("5. 'Lagarto' come a Papel y envenena a Spock.")
else:
    print("¡Genial! Entonces ya sabes cómo jugar.")
time.sleep(1)    
input("Presiona Enter para continuar...")
print("A la cuenta de tres, elige escribe tuu opción:")
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)
playerOpcion = input("Elige tu opción: ").lower()
cpu = random.choice(list(opciones.keys()))
if(playerOpcion in opciones):
    matcheo(playerOpcion
, cpu, opciones, jugador)
else: print("Opción no válida. Por favor, elige una opción válida.")