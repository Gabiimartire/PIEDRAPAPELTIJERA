def matcheo(player, cpu, opciones, nombrePLayer):
    if player == cpu:
        resultado = "¡Empate!"
    elif cpu in opciones[player]:
        resultado = "¡Ganaste " + nombrePLayer.capitalize() + "!", opciones[player][cpu]
    else:
        resultado = "¡Perdiste " + nombrePLayer.capitalize() + ": " + opciones[cpu][player] + "!"
    return resultado