"""
Ejercicio 5: Envíos con Servicios Adicionales
Patrón de Diseño: Decorator (Estructural)
Descripción: Permite añadir dinámicamente funcionalidades adicionales a un objeto
(como cifrado o auditoría) sin alterar sus clases base ni crear subclases excesivas.
"""
from abc import ABC, abstractmethod

# ==========================================
# 1. COMPONENTE ABSTRACTO
# ==========================================
class Notificacion(ABC):
    """Interfaz común tanto para el componente base como para los decoradores."""
    
    @abstractmethod
    def enviar(self, mensaje: str) -> str:
        pass


# ==========================================
# 2. COMPONENTE CONCRETO
# ==========================================
class NotificacionBasica(Notificacion):
    """Implementación base que realiza el envío estándar del mensaje."""
    
    def enviar(self, mensaje: str) -> str:
        print(f"[NOTIFICACIÓN BÁSICA] Enviando mensaje: '{mensaje}'")
        return mensaje


# ==========================================
# 3. DECORADOR BASE
# ==========================================
class NotificacionDecorador(Notificacion):
    """
    Decorador base. Mantiene una referencia a un objeto Notificacion
    y delega en él las operaciones por defecto.
    """
    
    def __init__(self, notificacion: Notificacion):
        self._notificacion = notificacion

    def enviar(self, mensaje: str) -> str:
        return self._notificacion.enviar(mensaje)


# ==========================================
# 4. DECORADORES CONCRETOS
# ==========================================
class DecoradorCifrado(NotificacionDecorador):
    """Añade una capa de cifrado simulado al mensaje antes de enviarlo."""
    
    def enviar(self, mensaje: str) -> str:
        print(f"[DECORADOR CIFRADO] Aplicando cifrado de seguridad al contenido...")
        # Simulamos un cifrado invirtiendo el texto o alterándolo
        mensaje_cifrado = f"[CIPHERED]: {mensaje[::-1]}"
        return super().enviar(mensaje_cifrado)


class DecoradorAuditoria(NotificacionDecorador):
    """Añade un registro en la bitácora de auditoría antes y después del envío."""
    
    def enviar(self, mensaje: str) -> str:
        print(f"[DECORADOR AUDITORÍA] Registrando evento de envío en la bitácora...")
        resultado = super().enviar(mensaje)
        print(f"[DECORADOR AUDITORÍA] Auditoría completada con éxito.")
        return resultado


# ==========================================
# EJEMPLO DE EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    print("--- PRUEBA DEL PATRÓN DECORATOR ---")

    # 1. Notificación básica pura
    print("\n1. Enviando notificación estándar (sin decoradores):")
    notif_simple = NotificacionBasica()
    notif_simple.enviar("Bienvenido a la plataforma.")

    # 2. Notificación decorada con Cifrado
    print("\n2. Enviando notificación con Cifrado:")
    notif_cifrada = DecoradorCifrado(NotificacionBasica())
    notif_cifrada.enviar("Clave de acceso temporal: 987654")

    # 3. Notificación con múltiples decoradores anidados (Cifrado + Auditoría)
    print("\n3. Enviando notificación con Cifrado y Auditoría combinados:")
    notif_completa = DecoradorAuditoria(DecoradorCifrado(NotificacionBasica()))
    notif_completa.enviar("Transacción bancaria aprobada por $500.")