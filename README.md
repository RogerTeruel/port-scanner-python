
# Port Scanner en Python

Escáner de puertos TCP simple hecho en Python. Esta herramienta permite escanear un host definido por el usuario en un rango de puertos determinado.

---

# Características

- Escaneo rápido usando sockets
- Permite definir rango de puertos
- Muestra puertos abiertos
- Código comentado y educativo

---

# Requisitos

- Python 3.12 o superior

No requiere librerías externas.

---

# Cómo ejecutar el escáner desde PowerShell (Windows)
Abre PowerShell:
Pulsa Win + S, escribe PowerShell y abre la aplicación.

# Navega hasta el directorio donde tienes el archivo.
Por ejemplo, si el archivo está en tu escritorio dentro de una carpeta llamada new_projects:

cd "C:\Users\TU_USUARIO\Desktop\new_projects"

# Despues ejecuta el script pasando los argumentos: [EJEMPLO]

python port_scanner.py 127.0.0.1 1 1024

127.0.0.1 → Dirección IP del objetivo (puedes usar localhost)
1 → Puerto inicial
1024 → Puerto final


# Requisitos
Tener Python instalado y añadido al PATH del sistema.
Ejecutar desde PowerShell, CMD o terminal equivalente.

