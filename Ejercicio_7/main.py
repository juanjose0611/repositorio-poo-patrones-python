"""
Ejercicio 7: Estación Meteorológica Inteligente
Patrón de Diseño: Observer (Comportamiento)
Descripción: Notifica automáticamente a múltiples dispositivos de visualización
(pantallas LED, aplicaciones móviles, registros) cada vez que cambian las variables climáticas.
"""
from abc import ABC, abstractmethod

# 1. INTERFAZ OBSERVER (Observador)
class Observador(ABC):
    """Interfaz que deben implementar todos los dispositivos interesados en los cambios."""
    
    @abstractmethod
    def actualizar(self, temperatura: float, humedad: float, presion: float) -> None:
        pass


# 2. CLASE SUBJECT (Sujeto Observable)
class EstacionMeteorologica:
    """Sujeto que mantiene la lista de observadores y notifica cambios de estado."""
    
    def __init__(self):
        self._observadores = []
        self._temperatura = 0.0
        self._humedad = 0.0
        self._presion = 0.0

    def suscribir(self, observador: Observador) -> None:
        """Agrega un nuevo observador a la lista de notificaciones."""
        self._observadores.append(observador)
        print(f"[ESTACIÓN] Nuevo dispositivo suscrito al sistema.")

    def desuscribir(self, observador: Observador) -> None:
        """Elimina un observador de la lista."""
        self._observadores.remove(observador)
        print(f"[ESTACIÓN] Dispositivo dado de baja del sistema.")

    def notificar_observadores(self) -> None:
        """Envía la actualización a todos los dispositivos suscritos."""
        for observador in self._observadores:
            observador.actualizar(self._temperatura, self._humedad, self._presion)

    def establecer_mediciones(self, temperatura: float, humedad: float, presion: float) -> None:
        """Actualiza los datos climáticos y dispara las notificaciones automáticas."""
        print(f"\n[ESTACIÓN CLIMÁTICA] Nuevos datos detectados -> Temp: {temperatura}°C | Humedad: {humedad}% | Presión: {presion} hPa")
        self._temperatura = temperatura
        self._humedad = humedad
        self._presion = presion
        self.notificar_observadores()


# 3. OBSERVADORES CONCRETOS
class PantallaLED(Observador):
    """Dispositivo de visualización principal en la oficina central."""
    
    def actualizar(self, temperatura: float, humedad: float, presion: float) -> None:
        print(f"  --> [Pantalla LED Central]: Clima actualizado -> {temperatura}°C y {humedad}% de humedad.")


class AppMovil(Observador):
    """Aplicación móvil para notificar al usuario final en tiempo real."""
    
    def actualizar(self, temperatura: float, humedad: float, presion: float) -> None:
        print(f"  --> [App Móvil]: ¡Alerta de clima! La temperatura actual es de {temperatura}°C.")


class RegistroLogger(Observador):
    """Sistema de almacenamiento de datos para análisis histórico."""
    
    def actualizar(self, temperatura: float, humedad: float, presion: float) -> None:
        print(f"  --> [Sistema Logger]: Guardando registro en base de datos -> Temp: {temperatura}, Humedad: {humedad}, Presión: {presion}")


# EJEMPLO DE EJECUCIÓN
if __name__ == "__main__":
    print("--- PRUEBA DEL PATRÓN OBSERVER ---")

    # 1. Creamos la Estación Meteorológica (Sujeto)
    estacion = EstacionMeteorologica()

    # 2. Creamos los dispositivos (Observadores)
    pantalla = PantallaLED()
    app = AppMovil()
    logger = RegistroLogger()

    # 3. Suscribimos los dispositivos a la estación
    print("\nRegistrando dispositivos en la estación:")
    estacion.suscribir(pantalla)
    estacion.suscribir(app)

    # 4. Primera actualización climática del día
    estacion.establecer_mediciones(24.5, 60.0, 1013.2)

    # 5. Suscribimos un nuevo dispositivo sobre la marcha (el sistema Logger)
    print("\nAñadiendo el sistema de registro histórico (Logger) a mitad del proceso:")
    estacion.suscribir(logger)

    # 6. Segunda actualización climática
    estacion.establecer_mediciones(27.8, 55.2, 1011.5)