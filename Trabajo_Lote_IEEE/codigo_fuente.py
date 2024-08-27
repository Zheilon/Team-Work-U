#Este programa calcula el area
#De un lote triangular.
print("-- Determinar Área del Lote --")

#Solicita al usuario que ingrese la Longitud de la base.
base = float(input("Ingrese Largo del Lote: "))

#Solicita al usuario que ingrese la Longitud de la altura.
altura = float(input("Ingrese ancho del lote: "))

#Por medio de esta función se Calcula el área,
#Utilizando la fórmula del área del Triángulo.
def area(base, altura):
    return (base * altura) / 2

#Salida Obtenida.
print(f"Area | Lote: {area(base, altura)} Mts Cuadrados.")