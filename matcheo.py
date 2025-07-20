def matcheo(player, cpu, opciones):
    if(player in opciones):
        print(f"La CPU eligió: {cpu}")
    if player == cpu:
        print("¡Empate!")
    elif cpu in opciones[player]:
        print("¡Ganaste!")
        print(opciones[player][cpu])
    else:
        print("¡Perdiste!")
        print(opciones[cpu][player])