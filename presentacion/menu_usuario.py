from negocio.perfil_usuario import CreadorPerfil, VistaPerfil
from negocio.compatibilidad import evaluar_compatibilidad
from negocio.notificacion import NotificadorMatch
from base_datos.perfiles_ficticios import obtener_perfiles

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

def mostrar_menu():
    print("=== Bienvenido al Sistema de Citas ===")
    print("\n🔐 Crea tu perfil:")
    perfil_usuario = crear_perfil_consola()
    vista_usuario = VistaPerfil(perfil_usuario)
    matches = []
    perfiles_disponibles = obtener_perfiles()
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
