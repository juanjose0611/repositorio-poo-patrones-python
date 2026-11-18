"""
Ejercicio 4: Adaptador de Pasarelas de Pago
Patrón de Diseño: Adapter (Estructural)
Descripción: Permite que clases con interfaces incompatibles trabajen juntas,
actuando como un traductor entre el sistema cliente y una pasarela de pago externa.
"""
from abc import ABC, abstractmethod

# ==========================================
# 1. INTERFAZ TARGET (Lo que espera nuestro sistema)
# ==========================================
class ProcesadorPago(ABC):
    """Interfaz estándar que nuestro sistema de comercio electrónico conoce y utiliza."""
    
    @abstractmethod
    def procesar_pago(self, monto: float) -> None:
        pass


# ==========================================
# 2. ADAPTEE / CLASE EXTERNA (Incompatible)
# ==========================================
class PasarelaStripeLegacy:
    """Sistema de pago externo heredado con métodos incompatibles."""
    
    def hacer_cargo(self, cantidad_en_centavos: int) -> None:
        print(f"[STRIPE LEGACY API] Procesando cargo de {cantidad_en_centavos} centavos en los servidores externos...")


# ==========================================
# 3. ADAPTER (El Adaptador / Traductor)
# ==========================================
class StripeAdapter(ProcesadorPago):
    """
    Adaptador que implementa la interfaz del sistema (ProcesadorPago)
    y traduce las llamadas hacia la clase externa (PasarelaStripeLegacy).
    """
    
    def __init__(self, pasarela_legacy: PasarelaStripeLegacy):
        self._pasarela_legacy = pasarela_legacy

    def procesar_pago(self, monto: float) -> None:
        # Traducción de datos:
        # 1. Convertimos el monto de formato estándar (ej. 150.50 $) a centavos (15050)
        centavos = int(monto * 100)
        
        print(f"[ADAPTER] Traduciendo pago de ${monto:.2f} a {centavos} centavos para Stripe...")
        
        # 2. Llamamos al método incompatible de la API externa
        self._pasarela_legacy.hacer_cargo(centavos)


# ==========================================
# EJEMPLO DE EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    print("--- PRUEBA DEL PATRÓN ADAPTER ---")

    # Simulamos el monto de una compra en el carrito de la tienda
    monto_compra = 99.99

    print(f"\n1. Intentando procesar pago mediante el adaptador de Stripe:")
    # Instanciamos la pasarela externa incompatible
    pasarela_externa = PasarelaStripeLegacy()
    
    # La envolvemos dentro de nuestro adaptador para que cumpla con la interfaz requerida
    procesador_adaptado: ProcesadorPago = StripeAdapter(pasarela_externa)
    
    # El sistema cliente utiliza el método estándar sin enterarse de las diferencias internas
    procesador_adaptado.procesar_pago(monto_compra)