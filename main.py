import time
import random
from matcheo import matcheo
print("¡Bienvenido al juego de Piedra, Papel, Tijera, Lagarto o Spock!")
time.sleep(1)
opciones = {
    'piedra':{'tijera': "Piedra aplasta a Tijeras", 'lagarto': 'Piedra aplasta a Lagarto'},
    'papel': {'piedra': "Papel cubre a Piedra", 'spock': "Papel refuta a Spock"},
    'tijera': {'papel': "Tijeras cortan a Papel", 'lagarto': "Tijeras decapitan a Lagarto"},
    'spock': {'tijera': "Spock destroza a Tijeras", 'piedra': "Spock vaporiza a Piedra"},
    'lagarto': {'papel': "Lagarto come a Papel", 'spock': "Lagarto envenena a Spock"}
}
print("Opciones disponibles:") 
for i, opcion in enumerate(opciones):
    print(f"{i + 1}. {opcion}")
print("A la cuenta de tres, elige tu opción:")
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)
jugador = input("Elige tu opción: ").lower()
cpu = random.choice(list(opciones.keys()))
if(jugador in opciones):
    matcheo(jugador, cpu, opciones)
else: print("Opción no válida. Por favor, elige una opción válida.")