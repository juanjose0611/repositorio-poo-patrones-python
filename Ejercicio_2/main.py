"""
Ejercicio 2: Fábrica de Notificaciones
Patrón de Diseño: Factory Method (Creacional)
Descripción: Desacopla la creación de objetos de notificación (Email, SMS, Push)
utilizando una jerarquía de fábricas especializadas.
"""
from abc import ABC, abstractmethod

# ==========================================
# 1. PRODUCTO ABSTRACTO
# ==========================================
class Notificacion(ABC):
    """Interfaz abstracta que define el producto común."""
    
    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        pass


# ==========================================
# 2. PRODUCTOS CONCRETOS
# ==========================================
class NotificacionEmail(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"[EMAIL] Enviando correo electrónico: '{mensaje}'")


class NotificacionSMS(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"[SMS] Enviando mensaje de texto SMS: '{mensaje}'")


class NotificacionPush(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"[PUSH] Enviando notificación push al dispositivo: '{mensaje}'")


# ==========================================
# 3. CREADOR (FÁBRICA) ABSTRACTO
# ==========================================
class CreadorNotificacion(ABC):
    """Clase creadora que define el Factory Method."""

    @abstractmethod
    def crear_notificacion(self) -> Notificacion:
        """Método de fábrica que las subclases implementarán."""
        pass

    def procesar_envio(self, mensaje: str) -> None:
        """Método de negocio que utiliza el objeto creado sin importarle su tipo exacto."""
        notificacion = self.crear_notificacion()
        print("[LOG] Preparando sistema de envío...")
        notificacion.enviar(mensaje)


# ==========================================
# 4. CREADORES CONCRETOS (FÁBRICAS ESPECÍfICAS)
# ==========================================
class CreadorEmail(CreadorNotificacion):
    def crear_notificacion(self) -> Notificacion:
        return NotificacionEmail()


class CreadorSMS(CreadorNotificacion):
    def crear_notificacion(self) -> Notificacion:
        return NotificacionSMS()


class CreadorPush(CreadorNotificacion):
    def crear_notificacion(self) -> Notificacion:
        return NotificacionPush()


# ==========================================
# EJEMPLO DE EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    print("--- PRUEBA DEL PATRÓN FACTORY METHOD ---")

    # Simulamos el envío a través de diferentes canales de forma desacoplada
    
    print("\n1. Canal seleccionado por el usuario: Email")
    fabrica_email = CreadorEmail()
    fabrica_email.procesar_envio("¡Su factura mensual está disponible para descarga!")

    print("\n2. Canal seleccionado por el usuario: SMS")
    fabrica_sms = CreadorSMS()
    fabrica_sms.procesar_envio("Su código de verificación de seguridad es: 9482")

    print("\n3. Canal seleccionado por el usuario: Push")
    fabrica_push = CreadorPush()
    fabrica_push.procesar_envio("Tienes un nuevo mensaje directo de tu equipo.")