"""
Ejercicio 3: Configurador de Vehículos Personalizados
Patrón de Diseño: Builder (Creacional)
Descripción: Permite construir objetos complejos (Vehículos) paso a paso,
separando el proceso de construcción de su representación final.
"""
from abc import ABC, abstractmethod

# ==========================================
# 1. PRODUCTO (Objeto complejo)
# ==========================================
class Vehiculo:
    def __init__(self):
        self.motor = None
        self.transmision = None
        self.color = None
        self.puertas = 0
        self.accesorios = []

    def mostrar_especificaciones(self):
        print(f"\n--- ESPECIFICACIONES DEL VEHÍCULO ---")
        print(f"Motor: {self.motor}")
        print(f"Transmisión: {self.transmision}")
        print(f"Color: {self.color}")
        print(f"Puertas: {self.puertas}")
        print(f"Accesorios: {', '.join(self.accesorios) if self.accesorios else 'Ninguno'}")
        print("-" * 40)


# ==========================================
# 2. BUILDER ABSTRACTO / INTERFAZ
# ==========================================
class IVehiculoBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_motor(self, motor: str):
        pass

    @abstractmethod
    def set_transmision(self, transmision: str):
        pass

    @abstractmethod
    def set_color(self, color: str):
        pass

    @abstractmethod
    def set_puertas(self, puertas: int):
        pass

    @abstractmethod
    def add_accesorio(self, accesorio: str):
        pass


# ==========================================
# 3. BUILDER CONCRETO
# ==========================================
class VehiculoBuilder(IVehiculoBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._vehiculo = Vehiculo()

    def set_motor(self, motor: str):
        self._vehiculo.motor = motor
        return self  # Permite encadenamiento de métodos (Fluent Interface)

    def set_transmision(self, transmision: str):
        self._vehiculo.transmision = transmision
        return self

    def set_color(self, color: str):
        self._vehiculo.color = color
        return self

    def set_puertas(self, puertas: int):
        self._vehiculo.puertas = puertas
        return self

    def add_accesorio(self, accesorio: str):
        self._vehiculo.accesorios.append(accesorio)
        return self

    def get_vehiculo(self) -> Vehiculo:
        vehiculo = self._vehiculo
        self.reset()  # Reiniciamos el builder para futuros usos
        return vehiculo


# ==========================================
# 4. DIRECTOR (Orquesta recetas predefinidas)
# ==========================================
class DirectorVehiculo:
    def __init__(self, builder: IVehiculoBuilder):
        self._builder = builder

    def construir_deportivo(self) -> Vehiculo:
        return (self._builder
                .set_motor("V8 Biturbo")
                .set_transmision("Automática Deportiva")
                .set_color("Rojo Ferrari")
                .set_puertas(2)
                .add_accesorio("Frenos cerámicos")
                .add_accesorio("Alerón de fibra de carbono")
                .get_vehiculo())

    def construir_camioneta(self) -> Vehiculo:
        return (self._builder
                .set_motor("Diesel 3.0 Turbo")
                .set_transmision("Manual 4x4")
                .set_color("Verde Militar")
                .set_puertas(4)
                .add_accesorio("Tracción 4x4 avanzada")
                .add_accesorio("Estribos laterales")
                .add_accesorio("Gancho de arrastre")
                .get_vehiculo())


# ==========================================
# EJEMPLO DE EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    print("--- PRUEBA DEL PATRÓN BUILDER ---")

    # Creamos el constructor (Builder) y el Director
    builder = VehiculoBuilder()
    director = DirectorVehiculo(builder)

    print("\n1. Construyendo un auto deportivo usando el Director:")
    deportivo = director.construir_deportivo()
    deportivo.mostrar_especificaciones()

    print("2. Construyendo una camioneta todoterreno usando el Director:")
    camioneta = director.construir_camioneta()
    camioneta.mostrar_especificaciones()

    print("3. Construyendo un vehículo personalizado paso a paso (sin Director):")
    auto_personalizado = (builder
                          .set_motor("Eléctrico de alto rendimiento")
                          .set_transmision("Automática Directa")
                          .set_color("Azul Metálico")
                          .set_puertas(4)
                          .add_accesorio("Piloto automático avanzado")
                          .add_accesorio("Techo panorámico")
                          .get_vehiculo())
    auto_personalizado.mostrar_especificaciones()