# Programa para calcular el promedio de tres notas

notas = []

for i in range(3):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)

print("\n--- RESULTADOS ---")
print(f"Notas ingresadas: {notas}")
print(f"Promedio final: {promedio:.2f}")
