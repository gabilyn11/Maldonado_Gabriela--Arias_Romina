import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0

    def lanzar_dado(self):
        valor = random.randint(1, 6)
        self.puntos += valor
        print(f"{self.nombre} sacó un {valor}. Total: {self.puntos}")

# --- PROGRAMA PRINCIPAL ---
j1 = Jugador("Usuario")
rival = Jugador("Bot")

for ronda in range(1, 4): # Juego de 3 rondas
    print(f"\n--- Ronda {ronda} ---")
    input("Presiona Enter para lanzar el dado...")
    j1.lanzar_dado()
    rival.lanzar_dado()

if j1.puntos > rival.puntos:
    print("\n¡Ganaste el desafío!")
else:
    print("\nEl Bot ganó esta vez.")

print("GAME OVER")