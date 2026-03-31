Elias Sosa - 028076/1
El proyecto sigue una estructura de directorios para separar el código en distintas partes:

1- `src/`: Contiene el código fuente principal.

2- `procesamiento.py`: Módulo que incluye las funciones encargadas de la lógica del negocio (cálculo de puntajes, determinación de ganadores por ronda e impresión de tablas).

3-`notebooks/`: Contiene el entorno de ejecución interactivo.

4-`entrega.ipynb`: Jupyter Notebook que importa las funciones de `src`, define el conjunto de datos de las rondas y ejecuta la simulación.

5-`requirements.txt`: Archivo con las dependencias necesarias para correr el proyecto.


## Requisitos Previos

Para ejecutar este proyecto, es necesario tener instalado:
* Tener descargado VS code: Programa que utilizamos para leer y ejecutar el programa
* [Python 3.8+](https://www.python.org/downloads/)
* Gestor de paquetes `pip`

## Instalación de Dependencias

1. Abrir una terminal en la carpeta raíz del proyecto (`PRACTICA-2-PYTHON`).
2. (Opcional pero recomendado) Crear y activar un entorno virtual.
3. Instalar las dependencias ejecutando el siguiente comando en cmd:

   ```bash
   pip install -r requirements.txt

Paso 1:
1. Descargá esta carpeta completa en tu computadora (asegurate de descomprimirla si está en un archivo .zip).
2. Abrí **Visual Studio Code**.
3. Andá arriba a la izquierda donde dice `Archivo` (o `File`) y elegí **`Abrir carpeta...`** (`Open Folder...`).
4. Buscá y seleccioná la carpeta principal de este proyecto (la que contiene todo).

**Paso 2:
1. A tu izquierda vas a ver los archivos del proyecto.
2. Hacé clic en la carpeta llamada **`notebooks`** para que se abra.
3. Adentro, hacé clic en el archivo llamado **`entrega.ipynb`**.


**Paso 3: ¡
1. Con el archivo `entrega.ipynb` abierto, vas a ver que arriba de todo el código hay un botón que dice **`Run All`** (o **`Ejecutar todo`**), que suele tener el ícono de dos flechitas o un botón de "Play".
2. Hacé clic ahí.
