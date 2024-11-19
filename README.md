# Optimización de Servicios y Herramientas para Windows

Este proyecto es una aplicación interactiva en formato ejecutable (`.exe`) para sistemas Windows. Incluye funcionalidades para la gestión de servicios, instalación de programas, descarga de repositorios y herramientas de escritorio, como la obtención de contraseñas Wi-Fi y la optimización de servicios.

## Funcionalidades

### Menú principal
La aplicación presenta un menú interactivo con las siguientes opciones principales:

1. **Instalar Programas**
   - Discord
   - Google Chrome
   - Python
   - Visual Studio Code

2. **Descargar Repositorios**
   - Reverse Shell en Python
   - RAT para Discord

3. **Herramientas de Escritorio**
   - Obtener la contraseña de la red Wi-Fi actual.
   - Optimización de servicios no esenciales.

4. **Salir**

### Características destacadas

- **Interfaz interactiva**: Menús accesibles y fáciles de navegar.
- **Automatización de servicios**: Optimiza y deshabilita servicios no esenciales del sistema Windows.
- **Gestión de redes Wi-Fi**: Obtiene el SSID y contraseña de la red Wi-Fi actual (si está disponible).
- **Ejecutable autónomo**: La aplicación se distribuye en formato `.exe`, lo que elimina la necesidad de instalar Python.

## Tecnologías y Librerías Usadas

- **Python**: Lenguaje en el que fue desarrollado inicialmente el código.
- **subprocess**: Para ejecutar comandos en el sistema.
- **os**: Para interactuar con el sistema operativo.
- **colorama**: Para dar formato con colores a la salida en la terminal.
- **PyInstaller**: Para convertir el script en un ejecutable `.exe`.

## Estructura del Proyecto

1. **Menú Principal**:
   - Navegación entre las funcionalidades principales.

2. **Submenús**:
   - **Instalación de programas**: Utiliza `winget` para instalar aplicaciones populares.
   - **Descarga de repositorios**: Clona proyectos desde GitHub.
   - **Herramientas de escritorio**: Incluye funcionalidades como obtención de contraseñas Wi-Fi y optimización de servicios.

3. **Funciones de utilidad**:
   - `disable_service`: Detiene y deshabilita servicios del sistema.
   - `get_wifi_password`: Obtiene el SSID y la contraseña de la red Wi-Fi actual.
   - `instalar_programa`: Ejecuta la instalación de aplicaciones.
   - `descargar_repositorio`: Descarga repositorios desde GitHub.

4. **Animación**:
   - `animated_ascii`: Genera una animación de bienvenida con arte ASCII.

## Cómo usar este proyecto

1. Descarga el archivo `.exe` desde la sección de [releases](https://github.com/tu-repo/releases).
2. Ejecuta el archivo `.exe` haciendo doble clic.
3. Sigue las instrucciones y selecciona las opciones desde el menú interactivo.

## Notas importantes

- Este ejecutable está diseñado exclusivamente para sistemas Windows.
- Algunas funcionalidades requieren permisos de administrador para ejecutarse correctamente, como la deshabilitación de servicios y la obtención de contraseñas Wi-Fi.
- **Advertencia**: Usa las funciones de esta aplicación con responsabilidad. Algunas acciones como la optimización de servicios pueden afectar el comportamiento de tu sistema.

## Licencia

Este proyecto se distribuye bajo la licencia [MIT](LICENSE).

---

¡Siéntete libre de colaborar o sugerir mejoras para este proyecto!
