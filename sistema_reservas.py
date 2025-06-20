# sistema_reservas.py

# Esta clase representa a un cliente del hotel.
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"{self.nombre} (ID: {self.cedula})"


# Esta clase representa una habitación de hotel.
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False  # Atributo para saber si está disponible

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            return True
        else:
            return False

    def liberar(self):
        self.ocupada = False


# Esta clase une cliente y habitación y calcula el costo total.
class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias
        self.total = dias * habitacion.precio

    def mostrar_reserva(self):
        return (f"Reserva para {self.cliente}\n"
                f"Habitación {self.habitacion.numero} ({self.habitacion.tipo})\n"
                f"Días: {self.dias} - Total: ${self.total:.2f}")


# --- Bloque principal para simular el sistema ---
if __name__ == "__main__":
    cliente1 = Cliente("Juan Pérez", "1102233445")
    habitacion1 = Habitacion(101, "Doble", 80)

    if habitacion1.reservar():
        reserva1 = Reserva(cliente1, habitacion1, 2)
        print(reserva1.mostrar_reserva())
    else:
        print("Habitación ocupada.")
