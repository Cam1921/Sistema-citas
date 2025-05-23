from negocio.perfil_usuario import Perfil

def obtener_perfiles():
    return [
        Perfil("Renata", 24, ["visitar museos", "natacion"], "virtual", "introvertida"),
        Perfil("Mathias", 27, ["deportes", "ver películas"], "presencial", "extrovertido"),
        Perfil("Samanta", 26, ["viajes", "escuchar musica"], "presencial", "extrovertida"),
        Perfil("Nicolas", 24, ["tecnología", "programar"], "virtual", "introvertido"),
        Perfil("Indira", 25, ["cine", "lectura"], "virtual", "extrovertida"),
        Perfil("Mateo", 30, ["Construción", "arte"], "presencial", "introvertido"),
    ]
