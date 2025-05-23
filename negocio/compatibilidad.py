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
