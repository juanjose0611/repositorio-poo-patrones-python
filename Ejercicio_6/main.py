"""
Ejercicio 6: Calculadora de Tarifas de Envío
Patrón de Diseño: Strategy (Comportamiento)
Descripción: Permite seleccionar dinámicamente diferentes algoritmos de cálculo
de tarifas de envío según la empresa transportadora elegida, evitando estructuras if-else complejas.
"""
from abc import ABC, abstractmethod

# ==========================================
# 1. INTERFAZ STRATEGY
# ==========================================
class EstrategiaEnvio(ABC):
    """Interfaz común que define el contrato para todos los algoritmos de envío."""
    
    @abstractmethod
    def calcular(self, peso_kg: float) -> float:
        pass


# ==========================================
# 2. ESTRATEGIAS CONCRETAS (Algoritmos específicos)
# ==========================================
class EnvioLocal(EstrategiaEnvio):
    """Tarifa económica para envíos dentro de la misma ciudad."""
    
    def calcular(self, peso_kg: float) -> float:
        tarifa_base = 5.0
        costo_por_kilo = 1.5
        total = tarifa_base + (peso_kg * costo_por_kilo)
        print(f"[COURIER LOCAL] Calculando envío local para {peso_kg} kg.")
        return total


class EnvioExpres(EstrategiaEnvio):
    """Tarifa rápida para envíos nacionales prioritarios."""
    
    def calcular(self, peso_kg: float) -> float:
        tarifa_base = 15.0
        costo_por_kilo = 3.5
        total = tarifa_base + (peso_kg * costo_por_kilo)
        print(f"[EXPRÉS] Calculando envío exprés prioritario para {peso_kg} kg.")
        return total


class EnvioAereo(EstrategiaEnvio):
    """Tarifa internacional o de carga pesada por vía aérea."""
    
    def calcular(self, peso_kg: float) -> float:
        tarifa_base = 30.0
        costo_por_kilo = 6.0
        total = tarifa_base + (peso_kg * costo_por_kilo)
        print(f"[AÉREO] Calculando carga aérea internacional para {peso_kg} kg.")
        return total


# ==========================================
# 3. CONTEXTO (Utiliza una estrategia)
# ==========================================
class CalculadoraEnvio:
    """Clase contexto que mantiene una referencia a una estrategia y la ejecuta."""
    
    def __init__(self, estrategia: EstrategiaEnvio):
        self._estrategia = estrategia

    def set_estrategia(self, estrategia: EstrategiaEnvio) -> None:
        """Permite cambiar la estrategia de cálculo en tiempo de ejecución."""
        self._estrategia = estrategia
        print(f"\n[INFO] Estrategia de envío cambiada exitosamente.")

    def cotizar(self, peso_kg: float) -> float:
        """Ejecuta el cálculo delegando en la estrategia actual configurada."""
        return self._estrategia.calcular(peso_kg)


# ==========================================
# EJEMPLO DE EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    print("--- PRUEBA DEL PATRÓN STRATEGY ---")
    peso_paquete = 4.5  # 4.5 kilogramos

    # 1. Seleccionamos inicialmente la estrategia de Envío Local
    calculadora = CalculadoraEnvio(EnvioLocal())
    costo = calculadora.cotizar(peso_paquete)
    print(f"Costo total del envío: ${costo:.2f}")

    # 2. El usuario cambia de opinión y selecciona Envío Exprés en tiempo de ejecución
    calculadora.set_estrategia(EnvioExpres())
    costo = calculadora.cotizar(peso_paquete)
    print(f"Costo total del envío: ${costo:.2f}")

    # 3. Finalmente, el usuario opta por Carga Aérea
    calculadora.set_estrategia(EnvioAereo())
    costo = calculadora.cotizar(peso_paquete)
    print(f"Costo total del envío: ${costo:.2f}")