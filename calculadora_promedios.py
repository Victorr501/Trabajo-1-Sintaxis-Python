def ingresar_calificaciones():
    nombres = []
    calificaciones = []
    
    while True:
        nombre = input("Ingrese el nombre de la materia: ")
        
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación para {nombre} (0-10): "))
                if 0 <= calificacion <= 10:
                    break
                else:
                    print("La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
        
        nombres.append(nombre)
        calificaciones.append(calificacion)
        
        continuar = input("¿Desea ingresar otra materia? (s/n): ").lower()
        if continuar != 's':
            break
            
    return nombres, calificaciones

def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

def determinar_estado(calificaciones, umbral=5.0):
    aprobadas = [i for i, cal in enumerate(calificaciones) if cal >= umbral]
    reprobadas = [i for i, cal in enumerate(calificaciones) if cal < umbral]
    return aprobadas, reprobadas

def encontrar_extremos(calificaciones):
    if not calificaciones:
        return None, None
    
    max_idx = calificaciones.index(max(calificaciones))
    min_idx = calificaciones.index(min(calificaciones))
    return max_idx, min_idx

def main():
    print("--- Calculadora de Promedios ---")
    nombres, calificaciones = ingresar_calificaciones()
    
    if not nombres:
        print("No se ingresaron materias.")
    else:
        promedio = calcular_promedio(calificaciones)
        aprobadas_idx, reprobadas_idx = determinar_estado(calificaciones)
        max_idx, min_idx = encontrar_extremos(calificaciones)
        
        print("--- Resumen Final ---")
        for i in range(len(nombres)):
            print(f"{nombres[i]}: {calificaciones[i]}")
        
        print(f"Promedio general: {promedio:.2f}")
        
        print("Materias aprobadas:")
        for idx in aprobadas_idx:
            print(f"- {nombres[idx]}")
            
        print("Materias reprobadas:")
        for idx in reprobadas_idx:
            print(f"- {nombres[idx]}")
            
        print(f"Mejor calificación: {nombres[max_idx]} con {calificaciones[max_idx]}")
        print(f"Peor calificación: {nombres[min_idx]} con {calificaciones[min_idx]}")
        
    print("¡Gracias por utilizar la calculadora! Adiós.")

if __name__ == "__main__":
    main()