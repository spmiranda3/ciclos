from unittest.util import sorted_list_difference


precios = []
for i in range(2):
    precios.append(int(input("Introduce un nuevo precio: ")))
print("Los precios son ingresados; ")
print(precios)
preciomax = max(precios)
print(preciomax)
