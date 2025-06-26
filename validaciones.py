def mostrar_juegos(dict):
    for j, dato in dict.items(): 
        print(j, dato)


def valida_pass(clave):
    Mayuscula=0
    Minuscula=0
    numero=0
    for palabra in clave:
        if palabra.isupper():
            Mayuscula+=1
        if palabra.islower():
            Minuscula+=1
        if palabra.isdigit():
            numero+=1
    if Mayuscula==2 and Minuscula==2 and numero==4 :
        print("la clave esta bien escrita ")
        return  True
    else:
         print("la clave está mal escrita ")
         return False


def valida_nombre(name):
    for n in name:
        if " "==n:
            return True
def valida_precio(preci):
    if preci>=8000 and preci<100000:
        return True
    else:
        return False

#el nombre debe tener por lo menos 2 palabras
#el precio debe estar entre 8000 y 1000000


def insertar_juego(dict):
    while True:
        nombre=input("ingrese el nombre ")
        if valida_nombre(nombre):
            break
        else:
            print("el nombre debe tener por lo menos 2 palabras")
    while True:        
        precio=int(input("ingrese el precio "))
        if valida_precio(precio):
            break
        else: 
            print("el precio debe estar entre 8000 y 1000000")
    while True:
        codigo=input("ingrese el codigo ")
        if valida_pass(codigo):
            pos=list(dict.keys())[-1]
            dict[pos+1]={"nombre":nombre, "precio":precio, "code":codigo}
            break
        else: 
            print('''
                No se agregó el juego. 
                El codigo del juego debe tener 2 mayusculas, 2 minusculas y 4 numeros
                ''')


def borrar_juegos(dict):
    mostrar_juegos(dict)
    borrar=int(input("que juego desea borrar? "))
    del juegos[borrar]


def actualizar_juego(dict):
    actualizar_juego(dict)
    actualizar=int(input("que juego va a actualizar? "))
    while True:
        print('''
                 1.- Nombre
                 2.- Precio
                 3.- Codigo
                 4.- Salir (volver a menu principal)
                 ''')
        dato=int(input("que dato va a actualizar? "))
        match dato:
            case 1:
               n=input("ingrese el nuevo nombre ")
               if valida_nombre (n):
                dict[actualizar]["nombre"]=n
               else: 
                   print("el nombre del juego debe tener al menos 2 palabras ")
            case 2:
               n=input("ingrese el nuevo precio ")
               if valida_precio(n):
                dict[actualizar]["precio"]=n
               else:
                   print("el precio debe estar entre 8000 y 1000000")
            case 3:
                n=input("ingrese el nuevo codigo ")
                if valida_pass(n):
                    dict[actualizar]["codigo"]=n
                else:
                    print("el parametro de la clave no es correcto ")
                    print('''
                        el codigo debe tener una mayuscula, una minuscula, un numero
                        y un largo exacto de 6
                        ''')





juegos={
    1:{"nombre": "pacman",
       "precio": "55000",
       "code": "MtDr2022"},
    2: {"nombre": "Zelda TOTK",
        "precio": "65000",
        "code": "QWkj2025"
        }
}


while True:
    try:
        print('''
            1.- Registrar un perro
            2.- Mostrar perros
            3.- Actualizar Perro
            4.- Borrar Perro
            5.- Salir
            ''')
        op=int(input("seleccione una opción "))
        match op:
            case 1:
                insertar_juego(juegos)
            case 2: 
                mostrar_juegos(juegos)
            case 3:
                valida_pass()
                actualizar_juego(juegos)
            case 4:
                borrar_juegos(juegos)
            case 5:
                break
            case _:
                  print("opción invalida ")
    except Exception as e:
        print("El error es: ", e)
