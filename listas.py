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
# 3.- crear boleta(mostrar cantidad de productos y sus precios, valor neto y valor+iva, )
# 4.- salir

# productos=["uva", "galleta oreo", "jabon"]
# precios=[2800, 1500, 3000]
# carrito=[]
# while True:
#     while True:
#         try:
#             print('''
#             1.- agregar productos (nombre del producto y precio)
#             2.- comprar
#             3.- crear boleta
#             4.- salir
#               ''')
#             op=int(input("seleccione una opción "))
#             break


#         except Exception:
#             print("SOLO NUMEROS ENTEROS ")
#     match op:
#         case 1:
#             prod=input("ingrese un producto: ")
#             productos.append(prod)
#             pre=int(input("ingrese el precio:  "))
#             precios.append(pre)
            
#         case 2:
#             while True:
#                 try:
#                     for i in range (len(productos)):
#                         print(i+1, productos[i], "$", precios[i] )
#                     producto=int(input("seleccione una opción "))
#                     break
#                 except Exception:
#                     print("SOLO NUMEROS ENTEROS ")
#             carrito.append(producto-1)
#             print(carrito)
#         case 3:
#             print("SU BOLETA ES: ")
#             for i in carrito:
#                 print(f"{productos[i]} $ {precios[i]}")
#                 total=total+precios[i]
#                 print("la cantidad de articulos que lleva es: ", len(carrito))
#                 print(f"el total de su compra es: {total} ")
#                 print(f"el total de su compra mas IVA es de: {total*1.19}")
                

        
#         case 4:
#             print("saliendo ")  
#             break     
#         case _:
#             print("opcion invalida ")


#################DICCIONARIOOOOOOOOOOOOOOOOOOOOOOOOOOOOS##########################
#ES UN COJUNTO DE PARES DE DATOS
# diccionario={
#     "nombre": "Pedro",
#     "numero": 12345,
#     "casado": False
# }
# #print(diccionario["nombre"])  COMO LLAMAR AL VALOR 
# print(diccionario)
# diccionario["ciudad"]="chiloe"
# print(diccionario)
# for key,value in diccionario.items(): 
#     #SE PUEDE PONER CUALQUIER VARIABLE AL FOR
#     print(key, value)
#     productos={
#         "manzana": 1200,
#         "melon": 2000,
#         "piña": 3000
#     }
#     productos["durazno"]=2500
#     print(productos)
#     nom=input("ingrese el nombre del producto: ")
#     valor=int(input("ingrese valor producto: "))
#     productos[nom]=valor

    # tareaaaa: actualizar carrito de compra con un diccionario

    ######19/06#########


frutas={
    "manzana": 1200,
    "melon": 2000,
    "piña": 3000
}
# frutas["durazno"]=2500
# print(frutas)
# nom=input("ingrese el nombre de producto ")
# valor=int(input("ingrese el valor producto: "))
# frutas[nom]=valor
# print(frutas)
while True:
    try:
        print('''
            1.- Ingresar fruta
            2.- Mostrar fruta
            3.- Actualizar precio
            4.- Eliminar producto
            5.-salir
              ''')
        op=int(input("seleccione una opción"))
        match op:
            case 1:
                fruta=input("ingrese el nombre de la fruta ")
            case 2:
                for key, dato in frutas.items(): #key, value son pares de datos
                    print(key, "$", dato )
            case 3:
                for key, dato in frutas.items():
                    print(key, "$", dato )
                actualizar=int(input("que precio de fruta va a actualizar? "))
                precio=int(input("ingrese el nuevo precio "))
                frutas[actualizar]=precio
                print("precio actualizado ")
            case 4:
                for key, dato in frutas.items():
                    print(key, "$", dato )
                eliminar=int(input("que fruta desea eliminar? "))
                del frutas[eliminar]
            case 5:
                print("saliendo")
                break
            case _:
                print("opcion no valida ")
    except Exception as e:
        print("el error es ", e)           
                
                
    