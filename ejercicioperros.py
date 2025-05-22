# perros de casa
# pida al usuario cantidad de perros
# muestre la cuota minima de conejos
# luego consulte cuantos conejos trajo
# si el perro trajo la cantidad minima
# cumplio la cuota, sino, se queda sin Filete 
# mostrar resumen de perro que cumplieron y los que no


import random 
import time
# while True:
#     try:
#          perros=int(input("ingrese la cantidad de perros "))
#          break
#     except Exception:
#          print("ingrese solo numeros, que sean mayor a 0 ")



# cantPerros=0
# cantidadperros=0
# conejosT=0


# perros=int(input("ingrese la cantidad de perros "))
# print("la cuota minima de conejos es 3 ")

# for i in range (perros):

#             conejos=random.randint(0, 6)
#             conejosT+=conejos
#             if conejos>=3:
#                 time.sleep(2)
#                 print(f"el perro trajo {conejos} ")
#                 print("cumplio la cuota, tiene filete ")
#                 cantPerros=cantPerros+1
#             else:
#                  time.sleep(2)
#                  print(f"el perro trajo {conejos} ")
#                  print("se queda sin filete ")
#                  cantidadperros=cantidadperros+1
# print(f"la cantidad de perros que cumplieron fueron {cantPerros} ")
# print(f"la cantiad de perros que no cumplieron fueron {cantidadperros} ")
####################### 
# while True:

#     try:
#         op=int(input("ingrese un numero: " ))
#         break
#     except Exception:
#         print("solo se permiten numeros enteros ")
#######################
# quiere pasar el ramo?
# pregunte la cantidad de rojos en el curso
# los talleres que hay en el semestre son 4
# por cada taller asistido tiene mas de un punto
# tiene la bendicion del profesor
# sino, no se le puede ayudar
# ingrese la nota final y sume las decimas acumuladas
# muestre si aprueba o reprueba
taller=0
notafinal=0

rojos=float("cuantos rojos hay en el curso? ")
for i in range (rojos):
    for Taller in range(talleres):
        decimas=0
        print(f"el alumno asistio al taller {t+1} ? ")
        resp=random.randint(1,2)
        if resp==1:
            decimas+=0.3
        if decimas>=1:
            print("tiene la bendicion del profesor ")
        else:
            print("no se le puede ayudar ")
    notafinal=float(input("cual es su nota final? "))  
    notafinal+=decimas
    if notafinal>=4:
        print("el alumno aprobo")
    else:
        print("usted no aprobo ")
##########################intento mio###################
    taller=input("por cada taller asistido tiene un punto, a cuantos talleres asistio? ")
    match:
    
    taller==1:
    print
    taller>=1:
        taller+=1
        print("tiene la bendicion del profesor ")
    else: 
        print("no se le puede ayudar ")

print(f"su nota final con las decimas acumuladas son {notafinal} ")
if notafinal>=4:
    print("usted aprobo ")
else:
    print("usted no aprobo ")








