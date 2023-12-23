#!/usr/bin/env python
# coding: utf-8

# In[9]:


from sklearn import tree

#Se crea la instancia del árbol de decisión.
clf = tree.DecisionTreeClassifier()

#[peso bruto, capacidad de carga, capacidad tanque combustible]
X = [[1368, 375, 9], [3311, 800, 26], [4100, 22018, 35], [1400, 429, 9], [2800, 750, 21], 
     [8500, 5667, 36], [1538, 470, 12], [2722, 793, 22], [7500, 4782, 36]]

#La salida donde se dice si es Sedan, Camioneta, Camion\n",
Y = ['Sedan', 'camioneta', 'camion', 'Sedan', 'camioneta', 'camion', 'Sedan', 'camioneta', 'camion']

#Se le pasa los datos  X y Y
clf = clf.fit(X, Y)

# Solicita datos al usuraio
print(" DIGITE LOS PARAMETROS ASI:")
PesoB = input("Digite el Peso Bruto del vehiculo Kg: ")
CapaC = input("Digite Capacidad de Carga : ")
CapaT = input("Digite Capacidad de combustible - Galones: ")
dato1 = [PesoB, CapaC, CapaT]
              
#Se muestra el resultado de prediccion de los datos ingresados.            
prediction = clf.predict([dato1])
              
#Se muestra el resultado de prediccion de los datos ingresados.
print("El tipo de auto corresponde a", prediction)


# In[ ]:




