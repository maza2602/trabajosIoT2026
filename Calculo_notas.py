# Programa para calcular las notas del duoc

def promedio_notas (notas_y_pesos):

    #lista de tuplas [(nota, peso), (nota, peso), .....]
    suma_notas = sum(nota * peso for nota, peso in notas_y_pesos)
    suma_pesos = sum(peso for _, peso in notas_y_pesos)

    if suma_pesos == 0:
        return 0
    
    return suma_notas / suma_pesos




mis_notas = [
    (7.0, 40),
    (4.0, 30),
    (4.0, 30)

]

promedio_notas = promedio_notas(mis_notas)
print(f'El promedio de notas es: {promedio_notas:.1f} ')
print(f'La calificación de examen es: {(promedio_notas * 0.4):.1f}')