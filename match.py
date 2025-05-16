#uso y explicacion de match

# def suma():
#     n1=int(input("ingrese un número: "))
#     n2=int(input("ingrese otro número: "))
#     print("el resultado de la suma es ", n1+n2)

# def resta():
#     n1=int(input("ingrese un número: "))
#     n2=int(input("ingrese otro número: "))
#     print("el resultado de la resta es ", n1-n2)

# def multiplicación():
#     n1=int(input("ingrese un número: "))
#     n2=int(input("ingrese otro número: "))
#     print("el resultado de la multiplicación es ", n1*n2)

# def división():
#     try: 
#      n1=int(input("ingrese un número: "))
#      n2=int(input("ingrese otro número: "))
#      print("el resultado de la división es ", n1/n2)
#     except ZeroDivisionError: #as nombre_de_excepcion
#         print(f"se produjo una excepción: ") #{nombre_de_excepcion}")
    

    
# def calcu():
#     while True:

#         print('''
#             1.- suma
#             2.- resta
#             3.- multiplicación
#             4.- división  
#             5.- salir  
#               ''')

#         op=int(input("seleccione una opción "))

#         match op:
#             case 1:
#                 print ("suma")
#                 suma()
#             case 2:
#                 print ("resta")
#                 resta()
#             case 3: 
#                 print ("multiplicación")  
#                 multiplicación() 
#             case 4:
#                 print ("división")  
#                 división()   
#             case 5:
#                 break #Ó print("saliendo")
#             case _:
#                 print("opcion no válida ")

#un nuuevo menu recursivo
#debe tener 3 programas anteriormente
#el menu debe llamar a estas y ejecutar de manera correcta
#debe tener la opcion de salir
#y la opcion por defecto


# def farmacia():
    
#     print(''' 
#         1.- Diazepam $9000
# 		2.- Metametozona $18500
# 		3.- Oblea China $1000
#         4.- salir
#           ''')
#     op=int(input("elija que producto llevará"))
#     match op:
#         case 1:
#             print("usted lleva Diazepam ")
            
#         case 2: 
#             print("usted lleva Metadona ")
            
#         case 3:
#             print ("usted lleva Oblea China ")
           
#         case 4:
#             print("salir ")
#         case _: 
#             print("Error, selecione una opcion valida (1,2,3)")
       
# def votacion():
    
#     print('''
#         1.- Hulk
#         2.- Ironman 
#         ''')
#     voto=int(input("ingrese su voto "))
#     match voto:
#         case 1:
#             print("votó por Hulk ")
#         case 2: 
#             print("voto por Ironman ")
#         case 3:
#             print("su voto es nulo ")
#         case 4:
#             print("salir ")
#         case _: 
#             print("opcion invalida ")
# def supermercado():
    
#     print('''Selecciones un producto
#         "1.- Vaselina $ 2000
# 		"2.- Rimel $ 3000
# 		"3.- Algodon $4000
#           ''')
#     produ=int(input("qué producto comprará? "))
#     match produ:
#         case 1:
#             print("usted lleva vaselina ")
#         case 2:
#             print("usted lleva rimel ")
#         case 3:
#             print ("usted lleva algodón ")
#         case 4:
#             print("finalizar compra ")
#         case _: 
#             print("no existe el producto ")



# while True:
#     try:

#         print('''
#             1.- compra farmacia
#             2.- votar
#             3.- comprar en supermercado
#             4.- salir
#             5.- no existe esta opción   
#               ''')
#         opc=int(input("Eija una opción "))
#         match opc:
#             case 1:
#                 print("eligio compra en farmacia ")
#                 farmacia()
#             case 2:
#                 print("votar")
#                 votacion()
#             case 3:
#                 print("eligió supermercado ")
#                 supermercado()
#             case 4:
#                 print("salir ")
#     except ValueError as errorr:
#             print(f"error: {errorr}")
    

#crear un menú de carrito con las sgtes opciones
#1.- ingresar nombre del usuario, sera mostrado en la boleta con un saludo
# 2.- comprar, poner productos para poder comprar con su precio correspondiente ej producto $1000
# 3.- sacar boleta, calcular el precio neto y el precio mas IVA. mostrar totales y bonus, mostrar cantidad de articulos que lleva
# 4.- salir
# consideracion: por lo menos 3 productos, no hay limite de compra
# se puede salir en cualquier momento
# los montos de los productos son fijos.
    
# def nombre():
    nom=input("ingrese su nombre ")
    
total=0
cantidad=0
while True:
    nombre()
    print('''Selecciones un producto
            1.- Vaselina $2000
            2.- Rimel $3000
            3.- Algodon $4500
          ''')
    

    produ=int(input("qué producto comprará? "))
    match produ:
        case 1:
             print("usted lleva vaselina ")
             Vaselina=int(input("cuantas va a querer? "))
             total+=Vaselina*2000
             cantidad+=Vaselina
        case 2:
             print("usted lleva rimel ")
             rimel=int(input("cuantas va a querer? "))
             total+=rimel*3000
             cantidad+=rimel
             
        case 3:
             print ("usted lleva algodón ")
             algodón=int(input("cuantas va a querer? "))
             total+=algodón*45000
             cantidad+=algodón
            
        case 4:
             print("salir y finalizar compra ")
             print(f"usted lleva {cantidad} cantidad de productos ")
             print(f"el total de su precio neta es: {total}")
             print("el total de su boleta+IVA es: ", total*1.19)
             print(f"gracias {nom} por su preferencia, vuelva pronto")
        case _: 
            print("no existe el producto ")
        

    

    
    
    
    
    





