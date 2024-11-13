
# Configuración del Entorno Virtual y Dependencias

Este documento describe cómo configurar un entorno virtual en Python y cómo gestionar las dependencias para el proyecto, con instrucciones específicas para **Mac**, **Windows** y **Ubuntu**.

## Requisitos Previos
- Tener **Python 3.x** instalado.
- Tener acceso a la terminal o línea de comandos.

---

## 1. Configuración del Entorno Virtual

### 1.1. MacOS

1. **Instalar Python 3 (si no está instalado)**:
   Puedes instalar Python desde el [sitio oficial de Python](https://www.python.org/downloads/) o usando **Homebrew**:
   ```bash
   brew install python
   ```

2. **Crear un entorno virtual**:
   Abre la terminal y navega hasta el directorio del proyecto, luego ejecuta:
   ```bash
   python3 -m venv myenv
   ```

3. **Activar el entorno virtual**:
   ```bash
   source myenv/bin/activate
   ```

4. **Instalar dependencias**:
   Una vez el entorno esté activado, puedes instalar las dependencias necesarias:
   ```bash
   pip install matplotlib numpy scipy pandas
   ```

5. **Desactivar el entorno virtual**:
   Cuando hayas terminado, puedes desactivar el entorno virtual con:
   ```bash
   deactivate
   ```

### 1.2. Windows

1. **Instalar Python 3 (si no está instalado)**:
   Descarga e instala Python desde el [sitio oficial](https://www.python.org/downloads/).

2. **Crear un entorno virtual**:
   En la línea de comandos, navega hasta el directorio del proyecto y ejecuta:
   ```bash
   python -m venv myenv
   ```

3. **Activar el entorno virtual**:
   En el símbolo del sistema (CMD):
   ```bash
   myenv\Scriptsctivate
   ```

4. **Instalar dependencias**:
   Una vez el entorno esté activado, instala las dependencias necesarias:
   ```bash
   pip install matplotlib numpy scipy pandas
   ```

5. **Desactivar el entorno virtual**:
   Cuando hayas terminado, puedes desactivar el entorno virtual con:
   ```bash
   deactivate
   ```

### 1.3. Ubuntu

1. **Instalar Python 3 (si no está instalado)**:
   En la terminal, usa el siguiente comando para instalar Python 3:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```

2. **Crear un entorno virtual**:
   En el directorio de tu proyecto, ejecuta:
   ```bash
   python3 -m venv myenv
   ```

3. **Activar el entorno virtual**:
   ```bash
   source myenv/bin/activate
   ```

4. **Instalar dependencias**:
   Con el entorno activado, instala las librerías necesarias:
   ```bash
   pip install matplotlib numpy scipy pandas
   ```

5. **Desactivar el entorno virtual**:
   Para desactivar el entorno virtual, ejecuta:
   ```bash
   deactivate
   ```

---

## 2. Crear un archivo `requirements.txt`

Para gestionar las dependencias del proyecto, genera un archivo `requirements.txt`:

1. Asegúrate de que el entorno virtual esté activado:
   ```bash
   source myenv/bin/activate
   ```

2. Usa `pip freeze` para generar el archivo `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```

Este archivo puede ser usado por otros para instalar las mismas dependencias ejecutando:
```bash
pip install -r requirements.txt
```

---

## 3. Subir el Proyecto a GitHub

### 3.1. Ignorar el Entorno Virtual

Es importante que el entorno virtual no se suba a GitHub. Para ello, añade la carpeta del entorno virtual al archivo `.gitignore`:

1. Abre o crea un archivo `.gitignore` en la raíz del proyecto.
2. Añade la siguiente línea:
   ```
   myenv/
   ```

### 3.2. Subir el Proyecto

Para subir tu proyecto a GitHub, sigue estos pasos:

1. Asegúrate de que el entorno virtual esté desactivado:
   ```bash
   deactivate
   ```

2. Añade y sube tus archivos:
   ```bash
   git add .
   git commit -m "Subir proyecto con entorno virtual y requirements.txt"
   git push origin master
   ```

---

## 4. Instrucciones para Otros Usuarios

Para otros usuarios que deseen clonar el proyecto y configurar su propio entorno:

1. Clona el repositorio:
   ```bash
   git clone <url_del_repositorio>
   cd <nombre_del_repositorio>
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Instala las dependencias desde el archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

Ahora pueden ejecutar el proyecto en su propio entorno virtual.
