from datetime import datetime

# Clase que representa una reserva
class Reserva:
    def __init__(self, nombre, habitacion, fecha_inicio, fecha_fin):
        self.nombre = nombre
        self.habitacion = habitacion
        self.fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        self.fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")

    def __str__(self):
        return f"{self.nombre} - Habitación {self.habitacion} ({self.fecha_inicio.strftime('%d/%m/%Y')} a {self.fecha_fin.strftime('%d/%m/%Y')})"

    def se_solapa(self, otra):
        """Verifica si esta reserva se solapa con otra."""
        return self.habitacion == otra.habitacion and not (
            self.fecha_fin <= otra.fecha_inicio or self.fecha_inicio >= otra.fecha_fin
        )

# Clase que gestiona las reservas del hotel
class Hotel:
    def __init__(self, total_habitaciones=10):
        self.total_habitaciones = total_habitaciones
        self.reservas = []

    def habitaciones_disponibles(self, fecha_inicio, fecha_fin):
        fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")
        ocupadas = set()

        for r in self.reservas:
            if not (fecha_fin <= r.fecha_inicio or fecha_inicio >= r.fecha_fin):
                ocupadas.add(r.habitacion)

        return [h for h in range(1, self.total_habitaciones + 1) if h not in ocupadas]

    def reservar(self):
        nombre = input("Nombre del cliente: ")
        fecha_inicio = input("Fecha de inicio (DD/MM/AAAA): ")
        fecha_fin = input("Fecha de fin (DD/MM/AAAA): ")

        disponibles = self.habitaciones_disponibles(fecha_inicio, fecha_fin)
        if not disponibles:
            print("No hay habitaciones disponibles en esas fechas.")
            return

        print("Habitaciones disponibles:", disponibles)
        habitacion = int(input("Seleccione una habitación: "))

        if habitacion not in disponibles:
            print("La habitación seleccionada no está disponible.")
            return

        nueva_reserva = Reserva(nombre, habitacion, fecha_inicio, fecha_fin)
        self.reservas.append(nueva_reserva)
        print("✅ Reserva realizada con éxito!")

    def mostrar_reservas(self):
        if not self.reservas:
            print("No hay reservas registradas.")
        else:
            print("\nReservas actuales:")
            for r in self.reservas:
                print(" -", r)

    def cancelar_reserva(self):
        nombre = input("Nombre del cliente para cancelar reserva: ")
        for r in self.reservas:
            if r.nombre.lower() == nombre.lower():
                self.reservas.remove(r)
                print("✅ Reserva cancelada exitosamente.")
                return
        print("No se encontró reserva con ese nombre.")

# Menú de consola
def main():
    hotel = Hotel(total_habitaciones=5)  # Puedes cambiar la cantidad de habitaciones
    while True:
        print("\n--- Sistema de Reservas Hotel ---")
        print("1. Hacer reserva")
        print("2. Consultar reservas")
        print("3. Cancelar reserva")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            hotel.reservar()
        elif opcion == "2":
            hotel.mostrar_reservas()
        elif opcion == "3":
            hotel.cancelar_reserva()
        elif opcion == "4":
            print("Gracias por usar el sistema.")
            break
        else:
            print("❌ Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
