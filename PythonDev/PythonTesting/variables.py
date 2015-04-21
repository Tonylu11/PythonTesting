'''
Created on 15/4/2015

@author: Antonio Luque Bravo
'''

a = 1
print a
print "Id 'a'", id(a), type(a)
print "Id '1'", id(1), type(1)
# a real
a = 2.5
print a
print "Id 'a'", id(a), type(a)
print "Id '2.5'", id(2.5), type(2.5)

# Lista
lista = [1, 2, 3, 4, 5]
print lista
print "Id 'lista'", id(lista), type(lista)
lista.append(6)
print lista
print "Id 'lista'", id(lista), type(lista)
lista2 = lista
print "Id 'lista'", id(lista), type(lista)
print "Id 'lista2'", id(lista2), type(lista2)
lista = ["1", "2", "3", "4", "5"]
print lista
print lista2
print "Id 'lista'", id(lista), type(lista)
print "Id 'lista2'", id(lista2), type(lista)





