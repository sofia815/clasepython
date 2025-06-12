#uso y ejemplos de listas
#       -5   -4 -3  -2 -1
# numeros=[10, 5, 9, 34, 20, ]
#        0   1  2   3   4
# print(numeros)
#numeros.reverse()     para poner numeros al reves
# for numero in numeros:
#     print("numero", numero*3)
# numeros.append(64)
# print(numeros)

# frutas=["durazno", "naranja", "manzana", "pera"]
# for fruta in frutas:
#     print(fruta)
    #Runtime(tiempo de ejecución): cuando corre mi programa
# nombres=[]
# while True:
#     print('''
#         1.- ingresa un nombre
#         2.- salir 
#           ''')
#     op=int(input("seleccione una opcion "))
#     match op:
#         case 1:
#             persona=input("ingrese un nombre ")
#             nombres.append(persona)
#             print(nombres)
#         case 2:
#             print("saliendo")
#             break
#         case _:
#             print("opcion invalida ")
#otro ejemplo
# nombres=["steven", "george"]
# apellidos=["spilvergo", "lucrecia"]
# while True:
#     print('''
#         1.- ingresa un nombre y apellido
#         2.- buscar nombre
#         3.- mostar nombres y apellidos
#         4.- salir 
#           ''')
    # op=int(input("seleccione una opcion "))
    # match op:
    #     case 1:
    #         persona=input("ingrese un nombre ")
    #         nombres.append(persona)
    #         apelli=input("ingrese un apellido ")
    #         apellidos.append(apellidos)
    #         print(nombres)
    #         print(len(nombres))
    #     case 2:
    #         buscar=input("ingrese un nombre a buscar: ")
    #         if buscar in nombres:
    #             print(f"el nombre {buscar} si está ")
    #         else: 
    #             print(f"el nombre {buscar} no está ")

    #     case 3:
    #         # c=0
    #         # for nombre in nombres:
    #         #     print(nombres[c], apellidos[c] )
    #         #     c+=1
    #         for i in range (len(nombres)):
    #             print(nombres[i], apellidos[i] )
    #     case 4:
    #         print("saliendo ")  
    #         break     
    #     case _:
    #         print("opcion invalida ")
#########TAREAA
# seleccione una opccion
# 1.- agregar productos (nombre del producto y precio)
# 2.- comprar(submenu mostrando productos y precios)
# 3.- crear boleta
# 4.- salir

productos=["1kg uva", "galleta oreo", "pan", "jabon"]
precios=[2800, 1500, 1000, 3000]
carrito=[]
while True:
    print('''
        1.- agregar productos (nombre del producto y precio)
        2.- comprar
        3.- crear boleta
        4.- salir
          ''')
    