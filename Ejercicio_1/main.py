"""
Ejercicio 1: Gestor de Configuración Global
Patrón de Diseño: Singleton (Creacional)
Descripción: Garantiza que exista una única instancia del sistema de configuración
en toda la aplicación, asegurando un punto de acceso global y consistente.
"""

class ConfiguracionGlobal:
    # Atributo de clase para almacenar la única instancia permitida
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            # Si la instancia no existe, la creamos usando la clase base object
            print("[LOG] Creando la ÚNICA instancia de ConfiguraciónGlobal (Singleton)...")
            cls._instancia = super(ConfiguracionGlobal, cls).__new__(cls)
            
            # Inicializamos las propiedades de configuración por única vez
            cls._instancia.modo_oscuro = True
            cls._instancia.idioma = "Español"
            cls._instancia.version_sistema = "1.0.0"
        else:
            print("[LOG] La instancia ya existía. Reutilizando la misma instancia...")
        return cls._instancia

    def mostrar_configuracion(self):
        """Muestra los valores actuales de la configuración."""
        print(f"\n--- CONFIGURACIÓN ACTUAL ---")
        print(f"Modo Oscuro: {self.modo_oscuro}")
        print(f"Idioma: {self.idioma}")
        print(f"Versión del Sistema: {self.version_sistema}")
        print("-" * 30)

    def cambiar_idioma(self, nuevo_idioma: str):
        """Permite modificar una propiedad de la configuración global."""
        self.idioma = nuevo_idioma
        print(f"[INFO] Idioma cambiado exitosamente a: {self.idioma}")


# ==========================================
# EJEMPLO DE EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    print("--- PRUEBA DEL PATRÓN SINGLETON ---")
    
    # 1. Intentamos crear la primera referencia a la configuración
    config1 = ConfiguracionGlobal()
    config1.mostrar_configuracion()

    # 2. Intentamos crear una "segunda" instancia en otra parte del sistema
    config2 = ConfiguracionGlobal()
    
    # 3. Verificamos si ambas variables apuntan exactamente al mismo objeto en memoria
    print(f"\n¿config1 y config2 son exactamente el mismo objeto?: {config1 is config2}")

    # 4. Modificamos el idioma usando la segunda variable (config2)
    config2.cambiar_idioma("Inglés")

    # 5. Comprobamos que los cambios se reflejan en la primera variable (config1)
    print("\nVerificando desde la primera referencia (config1):")
    config1.mostrar_configuracion()