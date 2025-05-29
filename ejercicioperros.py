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
# taller=0
# notafinal=0

# rojos=float("cuantos rojos hay en el curso? ")
# for i in range (rojos):
#     for Taller in range(talleres):
#         decimas=0
#         print(f"el alumno asistio al taller {t+1} ? ")
#         resp=random.randint(1,2)
#         if resp==1:
#             decimas+=0.3
#         if decimas>=1:
#             print("tiene la bendicion del profesor ")
#         else:
#             print("no se le puede ayudar ")
#     notafinal=float(input("cual es su nota final? "))  
#     notafinal+=decimas
#     if notafinal>=4:
#         print("el alumno aprobo")
#     else:
#         print("usted no aprobo ")
# ##########################intento mio###################
#     taller=input("por cada taller asistido tiene un punto, a cuantos talleres asistio? ")
#     match:
    
#     taller==1:
#     print
#     taller>=1:
#         taller+=1
#         print("tiene la bendicion del profesor ")
#     else: 
#         print("no se le puede ayudar ")

# print(f"su nota final con las decimas acumuladas son {notafinal} ")
# if notafinal>=4:
#     print("usted aprobo ")
# else:
#     print("usted no aprobo ")
####################################################################################23/05################################################################################

#crear menus con categorias
#cantarticulos=0
# total=0
# while True:
#     while True:
#         try:
#             print('''
#                 seleccione una opcion
#                   1.- teclados
#                   2.- monitores
#                   3.- audifonos
#                   4.- pagar
#                   5.- salir
#                 ''')
#             op=int(input())
#             break
#         except Exception:
#             print("ingrese un numero entero ")
#         match op:
#             case 1:
#                 print('''
#             seleccione una opcion
#               1.- teclado de manco $20000
#               2.- teclado gamer $40000
#               3.- teclado normal $8000
#               4.- volver a menu principal
#             ''')

#                 op=int(input())
#                 match op:
#                     case 1:
#                         total+=20000
#                         catarticulos+=1
#                     case 2:
#                         total+=40000
#                         catarticulos+=1
#                     case 3:
#                         total+=8000
#                         cantarticulos+=1
#                     case 4:
#                         break
#                     case _:
#                         print("opcion invalida ")
#                 print(f"el articulo agregado al carro lleva {cantarticulos} ")
#                 print(f"el total parcial es ${total}")

################################################################################################################################################


# El programa debe tener un menú de opciones de donde se pueda realizar el pago
# del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
# una vez sumadas se resten al cupo disponible.
# Las opciones disponibles deben estar construidas de la siguiente forma:
# 1. Pago de Tarjeta de Crédito:
# a. El usuario comienza con una deuda de $100.000
# b. El usuario puede ingresar un monto para realizar un pago en la
# tarjeta de crédito.
# c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d. Se debe verificar que el monto a pagar no exceda el saldo actual de
# la tarjeta.
# e. Al pagar el sistema debe descontar de la deuda total
# f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
# saldo de la tarjeta.
# 2. Simulación de Compras:
# a. El usuario puede simular realizar un número ilimitado de compras.
# b. Para cada compra, se solicita al usuario ingresar el monto de la
# compra. El programa suma los montos de cada compra.
# c. Se verifica que el monto de la compra sea mayor o igual a cero.
# d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
# iteración del bucle for.
# 3. Salir:
# a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
# A considerar:
# 1. Manejo de Errores:
# a. Se utilizan bloques try y except para manejar posibles errores al
# ingresar datos, validar valores no numéricos y errores inesperados.

# deuda=100000

# while True:
#     try:
#      print('''
#          1.- Pago de tarjeta de credito
#          2.- Simulacion de compras
#          3.- Salir
#      ''')
#      op=int(input("que desea realizar? "))
#     except Exception:
# #             print("ingrese un numero entero ")
#      match op:
#          case 1:
#              montopago=int(input("ingrese monto a pagar "))
#             if montopago>=0: and montopago<=saldotarjeta
#              print("")
#              print("")
#          case 2:



#                      op==3:
#                          print("saliendo...")

#################################################################################################################


# Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente caso:
# En un delivery de Sushi vende 4 tipos de Sushi:
# 1. Pikachu Roll $4500
# 2. Otaku Roll $5000
# 3. Pulpo Venenoso Roll $5200
# 4. Anguila Eléctrica Roll $4800
# La empresa le ha solicitado a usted, que genere una pequeña aplicación en Python para tomar el pedido de un
# cliente el cuál puede ir agregando Rolls a través de un menú uno por uno con solo seleccionar la opción (1 a 4)
# La aplicación debe mostrar en un menú los Rolls que agregará el usuario, esto se debe repetir hasta que el usuario
# decida que su pedido está completo.
# Luego de ello, debe preguntar al usuario si posee un código de descuento. En caso de que posea el código, deberá
# ingresarlo. Si el código ingresado es “soyotaku”, debe realizar un 10% de descuento al total del pedido, en caso
# contrario enviar el mensaje “código no válido” y dar al usuario la opción de reingresar el código o volver al menú
# tecleando “X”
# Una vez realizado los pasos anteriores, debe mostrar el detalle del pedido contabilizando el total de productos y la
# cantidad de cada uno de ellos y si aplica o no el descuento
# ******************************
# TOTAL PRODUCTOS:4
# ******************************
# Subdirección de Evaluación de Resultados de Aprendizaje - Subdirección de Diseño Instruccional 2- 2023 5
# Pikachu Roll : 2
# Otaku Roll :1
# Pulpo Venenoso Roll:1
# Anguila Eléctrica Roll:0
# ******************************
# Subtotal por pagar: $19200
# Descuento por código: $1920
# TOTAL: $17280
# Una vez que haya visualizado el detalle, debe preguntar al usuario si desea realizar otro pedido o salir del programa.
# Para finalizar suba el programa a un repositorio Github como respaldo y el link del repositorio a AVA en la actividad
# formativa 2 para aplicar la pauta de evaluación.
# total=0
# codigo="soyotaku"
# cant
# while True:
#         print ('''
#             1.- Pikachu Roll $4500
#             2.- Otaku Roll $5000
#             3.- Pulpo venenoso Roll $5200
#             4.- Anguila Electrica Roll $4800
#             5.- Salir
#             ''')
#         op=int(input("que desea pedir? "))
#         if op==1:
#                 print("eligio pikachu roll")
#                 total+=4500
#         elif op==2:
#                 print("eligio otaku roll")
#                 total+=5000
#         elif op==3:
#                 print("eligio pulpo ")
#                 total+=5200
#         elif op==4:
#                 print("eligio anguila electrica roll ")
#                 total+=4800
#         dcto=int(input("posee un codigo de descuento? /n 1.- SI /n 2.- NO "))
#         if op==1:
#             codigo=input(("ingrese su codigo "))
#             if codigo=="soyotaku":
#                    print(f"tiene un 10% de descuento ")
#             else:
#                    print("CODIGO NO VALIDO ")      



###################################29/05##########################################

# atletas de salto alto
# ingrese la cantidad de atletas que participaran
# cada atleta debe hacer un salto alto en el
# rango de 1.55mt y3.78 mt
#los atletas bajo 1.55: no califican
#entre 1.56 y 2 bronce
#entre 2.1 y 3 plata
#entre 3.1 y + adamantium
#poner la altura maxima lograda

# import random
# import time
# record=0
# atleta=0
# cantA=0
# atletas=int(input("cuantos atletas participaran? "))
# #atleta+=1
# for s in range (atletas):
#         salto=random.uniform(1.0, 3.78)
#         cantA+=salto
#         salto=cantA
#         print(f"el atleta n° {s+1} hizo un salto de {round(salto, 2)} metros")
#         if salto<1.55:
#                 print("no casifica ")
#         elif salto>=1.56 and salto<=2:
#                  time.sleep(2)
#                  print("el atleta obtuvo bronce ")
                         
#         elif salto>=2.1 and salto<=3:
#                  time.sleep(2)
#                  print("el atleta obtuvo plata ")
#         elif salto>=3.1:
#                  time.sleep(2)
#                  print("el atleta obtuvo adamantium ")
# print(f"el salto mas alto fue de {round(cantA,2)}")

#################################################################################################

# Libreria ñoña
# crear menu de comics
# 1. comprar
# 2. generar boleta
# 3. salir
# en la opcion de comprar, mostrar los comics con sus precios
# cuando se compra, mostrar la cantidad de articulos que lleva mas el monto neto y monto con IVA
# si ingresa el codigo de descuento "IAMBATMAN" obtiene 25% de dcto AL VALOR NETO
total=0
print("bienvenido a la libreria \n que desea hacer ")
op=int(input('''
        1.- comprar
        2.- generar boleta
        3.- salir
        '''))
match op:
        case 1:
                print("eligió la opcion comprar \n estas son sus opciones ")
                comic=int(input('''
                        1.- deadpool $10500
                        2.- x-men $12000
                        3.- spider man $15000 
                        4.- iron man 13500
                        5.- salir
                        '''))
                match comic:
                        case 1:
                                print("eligió deadpool ")
                                total+=10500
                        case 2:
                                print("eligió x-man ")
                                total+=12000
                        case 3:
                                print("espider man ")
                                total+=15000
                        case 4:
                                print("eligio iron man ")
                                total+=13500
                        case 5:
                                print("volviendo al menu principal ")
                        
        


