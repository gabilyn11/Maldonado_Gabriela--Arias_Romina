import random

class Hechicero:
    def __init__(self, nombre, vida, mana):
        self.nombre = nombre
        self.vida = vida
        self.mana = mana

    def lanzar_hechizo(self, objetivo):
        if self.mana >= 10:
            daño = random.randint(15, 25)
            self.mana -= 10
            objetivo.vida -= daño
            print(f"¡{self.nombre} lanza fuego! Daño: {daño}. Mana restante: {self.mana}")
        else:
            print(f"¡{self.nombre} no tiene suficiente mana!")

    def esta_vivo(self):
        return self.vida > 0

# --- PROGRAMA PRINCIPAL JUSTO ---
mago_usuario = Hechicero("Gandalf", 100, 40)
mago_rival = Hechicero("Gargamen", 100, 40)

while mago_usuario.esta_vivo() and mago_rival.esta_vivo():
    
    # 1. TURNO DEL JUGADOR
    if mago_usuario.mana >= 10:
        accion = input("\n¿Lanzar hechizo? (si/pasar): ").lower()
        if accion == "si":
            mago_usuario.lanzar_hechizo(mago_rival)
    else:
        print(f"\n{mago_usuario.nombre} no tiene maná para atacar...")

    # 2. CHEQUEO INTERMEDIO: ¿Murió el rival con el ataque?
    if not mago_rival.esta_vivo():
        break

    # 3. TURNO DEL RIVAL
    if mago_rival.mana >= 10:
        mago_rival.lanzar_hechizo(mago_usuario)
    else:
        print(f"{mago_rival.nombre} intenta atacar pero no tiene maná...")

    # 4. FINAL POR AGOTAMIENTO (Solo si AMBOS están sin maná)
    if mago_usuario.mana < 10 and mago_rival.mana < 10:
        print("\n--- ¡FIN DEL DUELO POR AGOTAMIENTO! ---")
        if mago_usuario.vida > mago_rival.vida:
            print(f"¡{mago_usuario.nombre} gana por puntos!")
        elif mago_rival.vida > mago_usuario.vida:
            print(f"¡{mago_rival.nombre} gana por puntos!")
        else:
            print("¡Empate técnico!")
        break

    print(f"VIDA -> {mago_usuario.nombre}: {mago_usuario.vida} | {mago_rival.nombre}: {mago_rival.vida}")

print("\nGAME OVER")


