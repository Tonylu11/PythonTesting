
import sys
print sys.maxint
a = 12323896274892643284232824243284234273423462842784263432723462734623468234872462347268428424624622
print a , type(a)
import math
print math.pi  # Numero PI
print 3 ** 2  # Potencias
print 10 ^ 10  # Operacion XOR Logica
print abs(-4321421)
print coerce(1, 924114L)
print pow(5, 2)  # potencias.
print round(66933.767)  # Redondear
print min(1.9999, 2, 4, 56, 7, 4, 12)  # Devuelve el minimo
print min("a", "A", "B", 23)  # Coje el primer caracter.
print "OTRA COSA"
a = 1
print a
print "CAMBIO"
a = b = c = 5
print a
print b
print c
print "CAMBIO 2"
a, b = 2, 3
print a
print b
print "TRUEQUE"
a, b = b, a
print a
print b
#CADENAS!!!!!
print "CADENAS EN PYTHON"
fruta = "platano"
fruta2 = 'platano'
print len(fruta)  # Calcula la longitud de el objeto "fruta"
print len(fruta2)  # Calcula la longitud de el objeto "fruta2"
print fruta[len(fruta) - 1]
print fruta[-3]
print "SLICES(REBANADAS DE CADENA)"
s = "Juan, Pedro y Maria"
print s[0:4]  # extrae la cadena desde la posicion 0 a la 3
print s[6:11]  # extrae la cadena desde la posicion 6 a la 10
print s[:11]  # extrae la cadena desde el principio hasta la posicion 10
print s[12:]  # extrae la cadena desde la posicion 12 hasta el final
print "Componer cadenas literales"
s = """una cadena larga"""
s = "me llamo\n juan"
print s
print "\tHola"
print r"\tHola"  # Con esa 'r' se ignora todos los saltos de linea
s = "juan"
print s
s = 'J' + s[1:]  # Anyade una J mayuscula y extrae la cadena desde la posicion 1 hasta el fin de la misma
print s
s = "Hola "
t = " y adios"
print s + t
print "Ahora multiplicamos con cadenas"
print s * 3 + t
# Para hacer una cadena mayusculas y minusculas (upper() para mayusculas y lower() para minusculas)
print "hola".upper()
print "ADIOS".lower()
print t.upper()
print s.upper()
e = s.upper()
print e
# expresiones dentro de las cadenas
print "hola %s son las %d horas" % ("juan", 5)
print "hola %s son las %+d horas" % ("juan", -5)
a = "Juan"
print a in "Juan"  # comprueba si a contiene la cadena "Juan" por ejemplo
print bool(a)  # comprueba si la cadena esta determinada, de ser asi devuelve true, si no false.
###############################################STRING#####################################################
import string
a = "asd asd asdas dasd asda sdsdadsa  dsdd sadsa da d ad asdsa dd"
print string.split(a)
print string.letters
print string.ascii_letters
print string.ascii_uppercase
print string.digits
print string.hexdigits
print string.octdigits
print string.punctuation
print string.find(a, "asd", 1, 12)
print string.replace(a, "asd", "cambiado")  # cambia asd por cambiado en la cadena a
print " SEPARADOR!!!!!!!!!!!!!!!!!!!!!!!"
lista=string.split(a)
print lista
print string.join(lista)