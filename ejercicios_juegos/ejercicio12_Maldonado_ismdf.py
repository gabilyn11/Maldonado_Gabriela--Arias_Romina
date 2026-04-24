class Aventurero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []

    def recoger(self, objeto):
        self.inventario.append(objeto)
        print(f"Has guardado: {objeto}")

    def mostrar_inventario(self):
        print(f"\nInventario de {self.nombre}: {self.inventario}")

    def usar_objeto(self):
        if self.inventario:
            objeto = self.inventario.pop(0) # Saca el primer objeto
            print(f"Has usado el objeto: {objeto}")
        else:
            print("El inventario está vacío.")

# --- PROGRAMA PRINCIPAL ---
player = Aventurero("zelda")
jugando = True

while jugando:
    accion = input("\n(1) Explorar (2) Ver Mochila (3) Usar algo (4) Salir: ")
    if accion == "1":
        item = input("¿Qué encontraste? ")
        player.recoger(item)
    elif accion == "2":
        player.mostrar_inventario()
    elif accion == "3":
        player.usar_objeto()
    elif accion == "4":
        jugando = False

print("\nGAME OVER")