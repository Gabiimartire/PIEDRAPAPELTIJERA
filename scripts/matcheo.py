def matcheo(player, cpu, opciones, nombrePLayer):
    if player == cpu:
        resultado = ("¡Empate!")
    elif cpu in opciones[player]:
        resultado = (f"¡Ganaste {nombrePLayer.capitalize()}!", opciones[player][cpu])
    else:
        resultado = (f"¡Perdiste {nombrePLayer.capitalize()}: {opciones[cpu][player]}!",)
    return resultado