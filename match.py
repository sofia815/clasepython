#uso y explicacion de match

def suma():
    n1=int(input("ingrese un número: "))
    n2=int(input("ingrese otro número: "))
    print("el resultado de la suma es ", n1+n2)

def resta():
    n1=int(input("ingrese un número: "))
    n2=int(input("ingrese otro número: "))
    print("el resultado de la resta es ", n1-n2)

def multiplicación():
    n1=int(input("ingrese un número: "))
    n2=int(input("ingrese otro número: "))
    print("el resultado de la multiplicación es ", n1*n2)

def división():
    try: 
     n1=int(input("ingrese un número: "))
     n2=int(input("ingrese otro número: "))
     print("el resultado de la división es ", n1/n2)
    except ZeroDivisionError: #as nombre_de_excepcion
        print(f"se produjo una excepción: ") #{nombre_de_excepcion}")
    

    

while True:

    print('''
        1.- suma
        2.- resta
        3.- multiplicación
        4.- división  
        5.- salir  
          ''')

    op=int(input("seleccione una opción "))

    match op:
        case 1:
            print ("suma")
            suma()
        case 2:
            print ("resta")
            resta()
        case 3: 
            print ("multiplicación")  
            multiplicación() 
        case 4:
            print ("división")  
            división()   
        case 5:
            break #Ó print("saliendo")
        case _:
            print("opcion no válida ")
