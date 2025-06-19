
import random
def clave():
    clave=3344
    password=int(input("Ingrese su pass :"))
    while clave!=password:
        print ("ERORR, clave invalida")
        password=int(input("Ingrese su pass :"))

    print("Bienvenido al sistema")

def ruleta():
    barril=random.randint(1,6)
    rul=int(input("Dispare"))

    while rul!=barril:
        rul=int(input("Dispare"))
    print("BANG!!!")

#funcion sin argumentos (nada entre parentesis)  #retorna a nada
def suma():
    n1=int(input("ingese el primer numero "))
    n2=int(input("ingrese otro numero "))
    print(n1+n2)
suma()  #para llamar funcion y mostrar en terminal 

#funcion con argumentos 
def suma_argumento(n1, n2):
    print(n1+n2)
suma_argumento(9, 8) 


#funcion con retornoo (retorna a un numero) sin argumento
def suma_ret():
    n1=int(input("ingese el primer numero "))
    n2=int(input("ingrese otro numero "))
    return n1+n2
#suma()
suma_argumento(9,8)
print (suma_ret())

#funcion con retorno y argumento
def suma_ret_arg(n1,n2):
    return n1+n2
print(suma_ret_arg(6,9))

def suma_3000(num):
    return num+3000
resultado=suma_3000(4000)
print(resultado)


def iva(numero):
    return numero*1.19
resultado=iva(4000)
print(resultado)

def descuento(precio, desc):
    return precio-(precio*desc/100)



#lista con diccionarios dentro
productos=[
    {"nombre":"lapiz", "precio": 400}, #indice 0 (diccionario 1)
    {"nombre":"goma", "precio" : 200},  #indice 1 (diccionario 2)
    {"nombre":"estuche", "precio" : 1600}  #indice 2 (diccionario 3)
]

print(productos[1])  #accedo a la lista, luego al diccionario, luego al valor

print(productos) #muestra mi lista actual
productos.append({"nombre":"papel lustre", "precio": 200})  #para agregar un nuevo elemento al final de la lista debo agregar otro diccionario
print(productos) #imprime lista actualizada

#tareaaaaaaaaaaaaaaaaaaaaaaa
1.- Agregar articulo
2.- Borrar Articulo
3.- Actualizar Articulo
4.- Mostrar listado de articulos
5.- Salir
'''
