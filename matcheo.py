def matcheo(player, cpu, opciones, nombrePLayer):
    if(player in opciones):
        print(f"La CPU eligió: {cpu}")
    if player == cpu:
        print("¡Empate!")
    elif cpu in opciones[player]:
        print(f"¡Ganaste {nombrePLayer.capitalize()}!")
        print(opciones[player][cpu])
    else:
        print(f"¡Perdiste {nombrePLayer.capitalize()}!")
        print(opciones[cpu][player])