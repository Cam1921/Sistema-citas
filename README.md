# Sistema de Citas por Consola

Este proyecto simula un sistema de citas estilo Tinder usando patrones de diseño.

## 🛠️ Tecnologías utilizadas

- Lenguaje: Python 3
- Interfaz: Terminal/Consola (no requiere GUI)
- Sin librerías externas

## 🔁 Patrones de diseño implementados

- 🧱 **Builder** – Clase `CreadorPerfil`: para construir objetos `Perfil` paso a paso
- 🧱 **Proxy** – Clase `VistaPerfil`: para mostrar resumen o vista completa del perfil
- 🧱 **Observer** – Clase `NotificadorMatch`: para notificar automáticamente cuando hay match

## ▶️ Cómo ejecutar

1. Abre tu terminal o consola
2. Posiciónate en la carpeta del proyecto
3. Ejecuta el siguiente comando:

```bash
python sistema_citas.py
