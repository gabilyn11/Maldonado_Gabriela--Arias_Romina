##duelo de rena (combate)
###clase la reseta (un tipo de objeto que nosotros podemos crear), para otener un objeto
##tener en cuenta las entidades y clases 

import random

class Personaje:
    def __init__(self, nombre, vida, daño):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño

    def atacar(self, objetivo):
        # Le restamos a la vida del objetivo nuestro daño
        objetivo.vida -= self.daño
        print(f"{self.nombre} ataca a {objetivo.nombre} y quita {self.daño} HP.")

    def esta_vivo(self):
        return self.vida > 0

# --- PROGRAMA PRINCIPAL ---
jugador = Personaje("Héroe", 100, 20)
rival = Personaje("Monstruo", 80, 20)

print("¡COMIENZA LA PELEA!")

while jugador.esta_vivo() and rival.esta_vivo():
    # Turno del usuario
    accion = input("\n¿Qué queres hacer? (atacar/esperar): ").lower()  # pasar todo a minusculas
    if accion == "atacar":
        jugador.atacar(rival)
    
    # Turno del rival (automático) si sigue vivo
    if rival.esta_vivo():
        rival.atacar(jugador)
    
    # Mostrar estado
    print(f"Estado -> {jugador.nombre}: {jugador.vida} | {rival.nombre}: {rival.vida}")

print("\nGAME OVER")

