def fun(a, b):  # parametros formales (entre parentesis)
    "Suma dos numeros cualesquiera que sean"  # Es una definicion de la funcion
    return a + b
x = fun(1, 43)  # Se utiliza la funcion definida mas arriba
print x
print fun.__doc__  # Muestra la documentacion ya definina mas arriba
def intercambia(a, b):
    return b, a  # Se pueden devolver mas de 1 valor.
y = intercambia(10, 32)
print y
def incrementa(a, b=1):
    return a + b
z = incrementa(1)  # Solo se define 1 porque b ya vale 1
print z
def fun2(i, *args):
    print " i=", i
    for arg in args:
        print arg, " tipo = ", type(arg)
print fun2(1,2,3,4,5,6,"hola")
