import random

def Correr():
      print('============================')
      print('  Bienvenidos al game ramdon')
      print('============================')

      rand = random.randint(0, 11)
      num_rand_user = int( input('Ingrese el numero: '))

      while num_rand_user != rand:
            if  num_rand_user < rand:
                  print('Ingresa un numero mas alto')
                  num_rand_user = int( input('Ingrese el numero: '))
            else:
                  print('Ingresa un numero mas bajo')
                  num_rand_user = int( input('Ingrese el numero: '))
      sumar = rand + num_rand_user*2

      print(f'Uhh! acertaste el numero {rand} que sumado y multiplicado es.. {sumar}')

if __name__=='__main__':
      Correr()