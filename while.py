#while.py
# clave=3344
# intentos=1
# password=int(input("ingrese su pass :"))

import random

# numAzar=random.randint(1,30)
# print(numAzar)

# #necesito al menos 20 puntos para abrir la puerta

# # if numAzar>=20:
# #     print("puede pasar")
# # else: 
# #     print("le falta puntaje")    

# #generar un numero aleatorio entre 1 y 50
# #pedir al usuario un numero
# #si ingresa un numero mayor decirle,
# #  "el numero a adivinar es menor"
# si ingresa un numero menor decirle
# "el numero a adivinar es mayor"
# ej numeroAadivinar=20
# si ingresa el 15 debe decir, "el numero es a adivinar es mayor"
# si ingresa el 35 debe decir "el numero a adivinar es menor"

# numeroAadivinar=random.randint(1,50)

# #print(numeroAadivinar)
# num=int(input("adivine el numero"))

# while num!=numeroAadivinar:
#     if num>numeroAadivinar:
#          print("el numero a adivinar es menor")
#     else:
#          print("el numero a adivinar es mayor")     
#     num=int(input("adivine el numero"))    
# print("le achuntaste")

#ruleta ruso
# barril=random.randint(1,6)
# ruleta=int(input("Dispare"))

# while ruleta!=barril:
#  ruleta=int(input("adivine el numero"))
#  print("bang!")

import time
#dado=0
# meta=30
# turno=1
# j1=0
#j2=0

# while j1<meta and j2<meta:
  
#     if turno % 2==0:
#         print("turno de j1")
#         time.sleep(5)
#         dado=random.randint(1,6)
#         j1+=dado
#         print(f"j1 saco {dado}")
#         print(f"avanza hasta la casilla {j1}")
#     else:
#         print("turno de j2")
#         time.sleep(5)
#         dado=random.randint(1,6)
#         j2+=dado
#         print(f"j2 saco {dado}")
#         print(f"avanza hasta la casilla {j2}")
#     turno+=1
#         # turno=turno+1

# #if j1>=meta or j2>=meta:
# if j1>j2:
#    print("El ganador es j1")
# else:
#  	print ("El ganador es j2")


#la florida 20%, la pintana 30%, pte alto 25%, san joaquin 15%
# grupo familiar: 1=>2%, 2 a 4=>3%, 5 o mas=>4%
# preguntar al usuario en que comuna vive
# preguntar al usuario con cuantas personas vive
# el arancel actual es de 200.000 por semestre
# basados en la respuestas del usuario y en
# la informacion dada, calculsr su dcto

# ej: ingrese su comuna
# ingrese su grupo familiar(num entero) : 4
# el total del dcto es 23%
# el total a pagar es $154.000

arancel=200000
dcto=0
print('''
     comunas:
    1.- Florida 20%
    2.- La Pintana 30%
    3.- Pte Alto 25%
    4.-San Joaquin 15%
     ''')
comuna=int(input("en que comuna vive?   "))
if comuna==1:
    dcto=20
elif comuna==2:
    dcto=30
elif comuna==3:
   dcto=25
elif comuna==4:
   dcto=15
else:
    print("seleccion incorecta")
   
grupofamiliar=int(input("con cuantas personas vive?")) #usted incluido
if grupofamiliar==1:
    dcto+=2
elif grupofamiliar<=4 and grupofamiliar>=2:
  dcto+=33
elif grupofamiliar>5:
     dcto+=4
else:
 print("seleccion incorrecta")
print("el dcto toal es ", dcto)
desc=arancel*dcto/100
total=arancel-desc
print("el total a pagar es $", total)