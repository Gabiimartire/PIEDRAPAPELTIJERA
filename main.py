import time
import random
from scripts.matcheo import matcheo
from scripts.reglas import mostrar_reglas
opciones = {
    'piedra':{'tijera': "Piedra aplasta a Tijeras", 'lagarto': 'Piedra aplasta a Lagarto'},
    'papel': {'piedra': "Papel cubre a Piedra", 'spock': "Papel refuta a Spock"},
    'tijera': {'papel': "Tijeras cortan a Papel", 'lagarto': "Tijeras decapitan a Lagarto"},
    'lagarto': {'papel': "Lagarto come a Papel", 'spock': "Lagarto envenena a Spock"},
    'spock': {'tijera': "Spock destroza a Tijeras", 'piedra': "Spock vaporiza a Piedra"}
}
print("¡Bienvenido al juego de Piedra, Papel, Tijera, Lagarto o Spock!")
time.sleep(1)
jugador = input("¿Cuál es tu nombre? ")
print(f"Hola, {jugador.capitalize()}! Vamos a jugar.")
time.sleep(1)
print("¿Sabes las reglas?")
reglas = input("Escribe 'sí' o 'no': ").lower()
if reglas == 'no':
    mostrar_reglas()
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
else: 
    print("Opción no válida. Por favor, elige una opción válida.")
    print(f"Las opciones válidas son: {', '.join([opcion.capitalize() for opcion in opciones.keys()])}.")