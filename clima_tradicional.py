# --- PROGRAMACIÓN TRADICIONAL ---

def obtener_temperatura_diaria(dia):
    """
    Solicita al usuario la temperatura para un día específico.
    Valida que la entrada sea un número flotante.
    """
    while True:
        try:
            temp_str = input(f"Ingrese la temperatura para el {dia}° día: ")
            temperatura = float(temp_str)
            return temperatura
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número para la temperatura.")

def calcular_promedio_semanal(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    """
    if not temperaturas: # Evitar división por cero si la lista está vacía
        return 0
    return sum(temperaturas) / len(temperaturas)

def main_tradicional():
    """
    Función principal para la ejecución del programa de programación tradicional.
    Recoge las temperaturas diarias y calcula el promedio semanal.
    """
    print("--- Calculadora de Promedio Semanal del Clima (Programación Tradicional) ---")
    dias_semana = 7
    temperaturas_semana = []

    for i in range(1, dias_semana + 1):
        temperatura = obtener_temperatura_diaria(i)
        temperaturas_semana.append(temperatura)

    promedio = calcular_promedio_semanal(temperaturas_semana)

    print("\n--- Resumen Semanal ---")
    for i, temp in enumerate(temperaturas_semana):
        print(f"Día {i+1}: {temp:.2f}°C")
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

# Punto de entrada para la ejecución del script
if __name__ == "__main__":
    main_tradicional()
