class Torre:
    def __init__(self, salud):
        self.salud = salud

    def recibir_daño(self, cantidad):
        self.salud -= cantidad
        print(f"¡La torre recibió un impacto! Salud actual: {self.salud}")

    def reparar(self):
        self.salud += 10
        print(f"Reparando... Salud actual: {self.salud}")

# --- PROGRAMA PRINCIPAL ---
defensa = Torre(50)

while defensa.salud > 0:
    print("\nEnemigos acercándose...")
    accion = input("¿Qué haces? (reparar/esperar): ").lower()
    
    if accion == "reparar":
        defensa.reparar()
    
    # El sistema ataca a la torre cada turno
    defensa.recibir_daño(15)

print("\n¡La torre ha caído! GAME OVER")