#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
from sklearn import tree
#Se crea la instancia del arbol de decision.
clf = tree.DecisionTreeClassifier()

#[altura, peso, talla de zapato]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

#La salida donde se dice si es hombre o mujer
Y = ['hombre', 'hombre', 'mujer', 'mujer', 'hombre', 'hombre', 'mujer', 'mujer',
     'mujer', 'hombre', 'hombre']


#Se le pasa los datos  X y Y para hacer el entrenamiento en el modelo
clf = clf.fit(X, Y)


#Se ingresan los datos para comparar con el modelo  
#Pueden ser unos datos fijos por ejemplo  dato1 = [190, 70, 43]
# Se ingresan a continuación los datos por consola

print(" Digite la siguiente información de la persona")
Altura = input("Digite altura en cm: ")
Peso   = input("Digite el peso en Kgs: ")
TallaC = input("Digite talla del calzado: ")
datos = [Altura, Peso, TallaC]


prediction = clf.predict([datos])

#Se muestra el resultado de la predicción de dato1
print("Segun los datos ingresados corresponden a:")
print(prediction)


# In[2]:


from sklearn import tree


#Se crea la instancia del árbol de decisión.

clf = tree.DecisionTreeClassifier()



#[altura, peso, talla de zapato]

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],

     [190, 90, 47], [175, 64, 39],

     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]



#La salida donde se dice si es hombre o mujer

Y = ['hombre', 'hombre', 'mujer', 'mujer', 'hombre', 'hombre', 'mujer', 'mujer',

     'mujer', 'hombre', 'hombre']



#Se le pasa los datos  X y Y

clf = clf.fit(X, Y)


#Se definen los datos 1 

dato1 = [190, 70, 43]

prediction = clf.predict([dato1])

#Se muestra el resultado de la predicción de dato1

print(prediction)


# In[3]:


from sklearn import tree

#Se crea la instancia del árbol de decisión.
clf = tree.DecisionTreeClassifier()

#[altura, peso, talla de zapato]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

#La salida donde se dice si es hombre o mujer
Y = ['hombre', 'hombre', 'mujer', 'mujer', 'hombre', 'hombre', 'mujer', 'mujer',
     'mujer', 'hombre', 'hombre']


#Se le pasa los datos  X y Y
clf = clf.fit(X, Y)


#Se definen los datos 1 
dato1 = [190, 70, 43]
prediction = clf.predict([dato1])

#Se muestra el resultado de la predicción de dato1

print(prediction)


# In[ ]:




