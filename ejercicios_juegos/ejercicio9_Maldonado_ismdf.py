import random

class Cofre:
    def __init__(self):
        # Definimos si está abierto y cuántas monedas tiene
        self.abierto = False
        self.monedas = random.randint(10, 50)

    def abrir(self):
        if not self.abierto:
            self.abierto = True
            print(f"¡Abriste el cofre y encontraste {self.monedas} monedas!")
            return self.monedas
        else:
            print("El cofre ya estaba abierto.")
            return 0

# --- PROGRAMA PRINCIPAL ---
total_monedas = 0
continuar = True

while continuar:
    print(f"\nExplorando la cueva... Tienes {total_monedas} monedas.")
    opcion = input("Encontraste un cofre. ¿Quieres intentar abrirlo? (si/no/salir): ").lower()
    
    if opcion == "si":
        nuevo_cofre = Cofre()
        total_monedas += nuevo_cofre.abrir()
    elif opcion == "salir":
        continuar = False
    else:
        print("Sigues caminando...")

print(f"\nFinalizaste con {total_monedas} monedas. GAME OVER")