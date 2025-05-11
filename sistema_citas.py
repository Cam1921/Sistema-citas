# === Patrón Builder ===
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

# === Patrón Proxy ===
# Proxy: controla el acceso a los datos completos del perfil
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

# === Patrón Observer ===
# Observer: permite reaccionar automáticamente cuando ocurre un match
class NotificadorMatch:
    def notificar(self, perfil1, perfil2):
        print(f"💘 ¡Match entre {perfil1.nombre} y {perfil2.nombre}!")

def crear_perfil_consola():
    creador = CreadorPerfil()
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    intereses = input("Intereses (separados por coma): ").split(",")
    tipo_cita = input("¿Prefieres citas presenciales o virtuales?: ").strip().lower()
    personalidad = input("¿Eres extrovertido o introvertido?: ").strip().lower()

    return creador.set_nombre(nombre)\
        .set_edad(edad)\
        .set_intereses([i.strip().lower() for i in intereses])\
        .set_tipo_cita(tipo_cita)\
        .set_personalidad(personalidad)\
        .construir()

def evaluar_compatibilidad(usuario, candidato):
    coincidencias = 0
    intereses_usuario = set([i.lower().strip() for i in usuario.intereses])
    intereses_candidato = set([i.lower().strip() for i in candidato.intereses])
    if intereses_usuario & intereses_candidato:
        coincidencias += 1
    if usuario.tipo_cita.lower().strip() == candidato.tipo_cita.lower().strip():
        coincidencias += 1
    if usuario.personalidad.lower().strip() == candidato.personalidad.lower().strip():
        coincidencias += 1
    return coincidencias >= 2

def main():
    print("=== Bienvenido al Sistema de Citas ===")
    print("\n🔐 Crea tu perfil:")
    perfil_usuario = crear_perfil_consola()
    vista_usuario = VistaPerfil(perfil_usuario)
    matches = []

    perfiles_disponibles = [
        Perfil("Ana", 24, ["arte", "música"], "presencial", "introvertido"),
        Perfil("Luis", 27, ["deportes", "películas"], "virtual", "extrovertido"),
        Perfil("Sara", 26, ["viajes", "lectura"], "presencial", "extrovertido"),
        Perfil("Carlos", 29, ["tecnología", "fútbol"], "virtual", "introvertido"),
        Perfil("Valentina", 25, ["cine", "lectura"], "virtual", "extrovertido"),
        Perfil("Mateo", 30, ["tecnología", "arte"], "presencial", "introvertido"),
    ]

    notificador = NotificadorMatch()

    while True:
        print("\n--- Menú ---")
        print("1. Ver perfiles disponibles")
        print("2. Ver matches")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            for p in perfiles_disponibles:
                vista = VistaPerfil(p)
                print("\nPerfil sugerido:")
                print(vista.mostrar_resumen())

                compatible = evaluar_compatibilidad(perfil_usuario, p)
                if compatible:
                    print("⚡ Alta compatibilidad detectada!")

                ver_mas = input("¿Deseas ver más información del perfil antes de hacer match? (s/n): ")
                if ver_mas.lower() == "s":
                    print(vista.mostrar_completo())

                r = input("¿Te gusta este perfil? (s/n): ")
                if r.lower() == "s":
                    notificador.notificar(perfil_usuario, p)
                    matches.append(p)
                    print("🔓 Acceso al perfil completo:")
                    print(vista.mostrar_completo())
                else:
                    print("⛔ Perfil descartado.")

        elif opcion == "2":
            print("\n💞 Tus Matches:")
            if matches:
                for m in matches:
                    print(f"- {m.nombre}, {m.edad} años, intereses: {', '.join(m.intereses)}")
            else:
                print("Aún no tienes matches.")

        elif opcion == "3":
            print("Gracias por usar el sistema de citas. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
