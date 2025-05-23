# --- Patrón Builder ---
class Perfil:
    def __init__(self, nombre, edad, intereses, tipo_cita, personalidad):
        self.nombre = nombre
        self.edad = edad
        self.intereses = intereses
        self.tipo_cita = tipo_cita
        self.personalidad = personalidad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

# Builder: permite construir objetos Perfil paso a paso
class CreadorPerfil:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.intereses = []
        self.tipo_cita = ""
        self.personalidad = ""

    def set_nombre(self, nombre):
        self.nombre = nombre
        return self

    def set_edad(self, edad):
        self.edad = edad
        return self

    def set_intereses(self, intereses):
        self.intereses = intereses
        return self

    def set_tipo_cita(self, tipo_cita):
        self.tipo_cita = tipo_cita
        return self

    def set_personalidad(self, personalidad):
        self.personalidad = personalidad
        return self

    def construir(self):
        return Perfil(self.nombre, self.edad, self.intereses, self.tipo_cita, self.personalidad)

# --- Patrón Proxy ---
class VistaPerfil:
    def __init__(self, perfil):
        self._perfil = perfil

    def mostrar_resumen(self):
        return (
            f"{self._perfil.nombre}, {self._perfil.edad} años\n"
            f"Prefiere citas: {self._perfil.tipo_cita}\n"
            f"Personalidad: {self._perfil.personalidad}"
        )

    def mostrar_completo(self):
        return (
            f"{self._perfil.nombre}, {self._perfil.edad} años\n"
            f"Intereses: {', '.join(self._perfil.intereses)}\n"
            f"Prefiere citas: {self._perfil.tipo_cita}\n"
            f"Personalidad: {self._perfil.personalidad}"
        )
