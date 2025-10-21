# Mini Core - Calculadora de Comisiones

Esta es una aplicación web full-stack diseñada para calcular las comisiones de los vendedores basándose en el total de sus ventas dentro de un rango de fechas específico.

## Tecnologías Utilizadas

### Backend
* **Python 3.10+**
* **FastAPI:** Para construir una API web rápida y moderna.
* **SQLAlchemy:** Como ORM para interactuar con la base de datos SQL.
* **Uvicorn:** Como servidor ASGI para ejecutar la aplicación.
* **Pydantic:** Para la validación de datos.

### Frontend
* **React 18+**
* **JavaScript (ES6+)**
* **HTML5 & CSS3**

---

## Guía de Instalación y Ejecución

Sigue estos pasos para levantar el proyecto en tu máquina local.

### **Prerrequisitos**
Asegúrate de tener instalado lo siguiente:
* [Git](https://git-scm.com/)
* [Python 3.10 o superior](https://www.python.org/downloads/)
* [Node.js y npm](https://nodejs.org/en/) (v16 o superior)

### **1. Configuración del Backend**

1.  **Clona el repositorio:**
    ```bash
    git clone <URL_DE_TU_REPOSITORIO>
    cd <NOMBRE_DE_TU_PROYECTO>
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # Crea el entorno
    python -m venv venv

    # Activa el entorno (Windows)
    .\venv\Scripts\activate

    # Activa el entorno (macOS/Linux)
    source venv/bin/activate
    ```

3.  **Instala las dependencias de Python:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Crea el archivo de configuración:** En la raíz del proyecto, crea un archivo llamado `.env` y añade la siguiente línea:
    ```.env
    DATABASE_URL="sqlite:///./comisiones.db"
    ```

5.  **Puebla la base de datos con datos de ejemplo:** Este comando creará la base de datos y la llenará con vendedores y ventas aleatorias para que puedas probar la aplicación.
    ```bash
    python seed.py
    ```

6.  **Ejecuta el servidor del backend:**
    ```bash
    uvicorn app.main:app --reload
    ```
    El backend ahora estará corriendo en `http://127.0.0.1:8000`.

### **2. Configuración del Frontend**

1.  **Abre una nueva terminal.** No cierres la terminal donde está corriendo el backend.

2.  **Navega a la carpeta del frontend:**
    ```bash
    cd frontend
    ```

3.  **Instala las dependencias de Node.js:**
    ```bash
    npm install
    ```

4.  **Ejecuta la aplicación de React:**
    ```bash
    npm start
    ```
    Tu navegador se abrirá automáticamente en `http://localhost:3000` con la aplicación funcionando.