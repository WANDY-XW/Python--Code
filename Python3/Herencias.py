# Clases de Herencia y Polimorfismo

from pip import main


class Persona:
      
      def __init__(self, name):
            self.name = name

      def Avanza(self):
            print("Ando Caminando")

class Ciclista(Persona):

      def __init__(self, name):
            super().__init__(name)

      def Avanza(self):
            print("Voy en la Bicicleta")

            

def main():
      persona = Persona("Wandy Olivares...")
      persona.Avanza()

      ciclista = Ciclista("Wandy Olivares")
      ciclista.Avanza()
      
if __name__ == "__main__":
      main()
# end main
      