from curses import pair_number
from os import initgroups
import random

# Adivina con quien hablas >>IA<<
def IAV():

      print("======================")
      print("    Hola soy  VI!     ")
      print("Existen Hasta ahora 2 personajes")
      print("       Pedro y Maria"         )
      print("======================")

      # Datos de Asistente V o Señor V
      AsistenteSV ={
            {"Name":     "Señor V",
            "Id":             "AVirtual ",
            "Oficio":         "Mayordomo",
            "Edad":    0,
            "Lastname": "Hey VI",},

      # Datos de Federico el loco
            {"Name":     "Federico",
            "Id":       "DF" ,
            "Oficio":  "Albañil",  
            "Edad":    90,
            "Lastname":  "La Calva"},

      #El Inteligente 
            {"Name":     "Daniel",
            "Id":       "HD" ,
            "Oficio":  "Hackers",  
            "Edad":    0,
            "Lastname":  "El Flow"},

      # La puta
            {"Name": "Arison",
            "Id":       "Marica",
            "Oficio": "Puta",
            "Edad": 25,
            "Lastname": "Ricky Martin"}   }


      print("Quieres continuar")
      ConfirS = input("Si: ") 
      print("O")
      ConfirN = input("No: ")

      if ConfirS == "S":
            Diccionario = {
                  
            "AjectivosP":     ["Simpático", "Abierto", "Extrovertido"
            "Alegre", "Persistente", "Sociable", "Comprensivo", "Imaginativo"],

            "AjetivosN":      ["Aburrido", "Malhumorado", "Malvado", 
            "Rencoroso", "Perezoso", "Descuidado", "Egoísta", "Terco", "Tacaño"],    }


            
            adjetivo = input('Adjetivo: ')
            sustantivo = "Oscuro"

            RAM = random.choice(Diccionario["AjectivosP"])
            Historia = f'Programar con {adjetivo} es divertido por que  es{sustantivo} y si, es genial!'

            print(Historia)
            
      else:
            print("")
      
if __name__ == '__main__':
      IAV()