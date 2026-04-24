import random

class Auto:
    def __init__(self, marca):
        self.marca = marca
        self.distancia = 0

    def avanzar(self):
        # El avance es aleatorio para los rivales
        pasos = random.randint(1, 10)
        self.distancia += pasos

    def nitro(self):
        # Acción especial del usuario
        self.distancia += 15
        print(f"¡{self.marca} usó NITRO!")

# --- PROGRAMA PRINCIPAL ---
mi_auto = Auto("Ferrari")
rival = Auto("Rival")

for ronda in range(1, 6): # Carrera de 5 turnos
    print(f"\n--- Turno {ronda} ---")
    accion = input("¿Qué hacer? (avanzar/nitro): ").lower()
    
    if accion == "nitro":
        mi_auto.nitro()
    else:
        mi_auto.avanzar()
    
    rival.avanzar() # El rival siempre avanza automático
    
    print(f"Posiciones -> {mi_auto.marca}: {mi_auto.distancia}m | {rival.marca}: {rival.distancia}m")

# Resultado final
if mi_auto.distancia > rival.distancia:
    print("\n¡Ganaste la carrera!")
else:
    print("\nPerdiste... el rival fue más rápido.")

print("GAME OVER")