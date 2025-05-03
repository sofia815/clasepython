# print("repaso general")

#declaracion de variables
# nombre="sofia"
# edad=64

#concatenacion
# print("hola", nombre, "su edad es", edad)
# print(f"hola{nombre} y su edad es {edad}")

#solicitud de variable
# nombre=input("ingrese nombre")
# edad=int(input("ingrese su edad"))

# print(f"hola {nombre}, su edad es {edad}")

#suma 2 numeros
#print("ingrese 2 numeros")
#n1=int(input())
#n2=int(input())

# print("la suma de los numeros es", n1+n2)

# explicacion y uso de for

# for i in range(3):
#     print(i+1)


    
# cantnotas=int(input("ingrese la cantidad de notas "))
# suma=0
# for i in range(cantnotas):
#      print(f"ingrese la nota numero {i+1}")
#      nota=float(input())
#      suma=suma+nota
# prom=suma/cantnotas
# print("el promedio es ", round(prom,1))

#explicacion y uso de librerias

import random
#otra forma es -
from random import randint
#
import time
# num1=random.randint(1,6)
# num2=randint(1,6)
# # print(num1, num2)


# for i in range(3):
#     time.sleep(1)
#     print(i+1)


#explicacion y uso de while

#num=0

# while num<5:
#     print("hola")
#     num+=1
#clave con intentos infitos
# clave=4455
# #1234
# #4455!=1234//si, por lo tanto esta afirmacion es verdadera osea true
# password=int(input("ingrese su clave"))
# while clave!=password:
#     print("error, intente nuevamente")
#     password=int(input("ingrese su password"))
# print("bienvenido al sistema")    

#clave con solo 3 intentos
# clave=3344
# intentos=3
# password=int(input("ingrese su clave"))
# while clave!=password or intentos ==0:
#     intentos-=1
#     print(f"errar, le quedan {intentos} intentos")
#     password=int(input("ingrese su clave : "))
#     if intentos<=1:
#         break
# if intentos!=0 and clave==password:
#     print("usted ingreso al sistema")
# else:
#     print("sistema bloqueado")        


#recorrer las letras de una frase con un for
# frase=input("ingrese una frase")

# for i in frase:
#     print(i)


#contar los autos que llegan al estacionamiento
#rojos, azules y otro color

# rojos=0
# azules=0
# otro=0
# while color==4
# color=int(input('''
#           ingrese el color del auto
#           1.- rojo
#           2.- azul
#           3.- otro
#           4.- salir      
#           '''))
# if color==1:
#  print("el color es rojo")
#  rojos+=1
# elif color==2:
#  print("el color es azul")
#  azules+=1
# elif color==3:
# else: 
#  print("saliendo")


# print("los autos de color rojo son", rojos)   




###EJERCICIO TIPO PRUEBA!!!###
#categorizar jugadores
#en una liga amateur, se paga a los jugadores de futbol
#cuando anota mas goles recibe un bno en su paga
#entre 1-3 goles, 4%; entre 4-6 goles 6%, 7 goles% o mas 8%
#si su equipo queda entre los 3 primeros, +3000
# si su equipo queda entre 4y 8, +2000
# si su equipo queda entre 9 y mas, +1000
#el pago base por jugar es de 5000

goles=randint(1,10)
print("los goles anotados en la temporada fueron ", goles)
time.sleep(1)
posicion=randint(1,16)
print("los posicion final en la temporada fue ", posicion)

# goles=int(input("cuantós goles anotó?"))
sueldo=5000
if goles>=1 and goles<=3:
    sueldo=sueldo*1.04
elif goles>4 and goles<1.06:
    sueldo=sueldo*1.06
else: 
    sueldo=sueldo*1.08

if posicion>=1 and posicion<=3:
    sueldo+=3000
elif posicion>=4 and posicion<=8:
    sueldo+=2000
else:
    sueldo+=1000
print("el total del sueldo del juagador al fnal de temporada es: ")                        
