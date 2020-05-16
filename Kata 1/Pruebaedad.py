mi_edad = 27
mi_nombre = "Joaquín"
soy_humano = True

mi_edad_mental = mi_edad - 12

print("Mi edad mental es:",mi_edad_mental)

# Formula cuadrados. Definimos qué se hace en cuadrado. Luego definimos donde se guarda la info de esa función.

def cuadrado(x):
    return x * x

cuadrado_de_dos = cuadrado(2)
print("El cuadrado de 2 es:",cuadrado_de_dos)

# Control y condiciones

if condicion == True:
    haz_tarea()
else:
    haz_otra_tarea()

for valor in (1,2,3,4):
    print(valor)
