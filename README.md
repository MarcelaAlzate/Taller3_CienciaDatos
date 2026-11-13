# Taller 3 - Bases de Datos para Ciencia de Datos

## Análisis de datos de personajes de Dragon Ball

Este proyecto realiza la extracción, almacenamiento y análisis exploratorio de datos de personajes de **Dragon Ball** utilizando una API pública, MongoDB y Python.

El proyecto permite obtener los datos desde la API, almacenarlos en MongoDB y posteriormente realizar un análisis exploratorio mediante Pandas y Jupyter Notebook.

## Tecnologías utilizadas

- Python
- MongoDB
- PyMongo
- Requests
- Pandas
- Matplotlib
- Jupyter Notebook
- Git y GitHub

## Fuente de datos

Los datos utilizados corresponden a personajes de Dragon Ball obtenidos mediante la **Dragon Ball API**.

La información obtenida incluye datos como:

- Nombre del personaje
- Raza
- Género
- Ki
- Ki máximo
- Afiliación
- Descripción

## Estructura del proyecto

```text
proyecto_taller3/
│
├── ingesta.py
├── analisis.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```

### `ingesta.py`

Script encargado de realizar la extracción de los datos desde la API y almacenarlos en MongoDB.

### `analisis.ipynb`

Notebook de Jupyter utilizado para realizar el análisis exploratorio de datos (EDA).

En este notebook se realizan:

- Conexión a MongoDB.
- Lectura de la colección.
- Selección de variables.
- Limpieza y transformación de datos.
- Inspección de los datos.
- Cálculo de cinco insights.
- Generación de tres gráficos.

### `requirements.txt`

Contiene las librerías necesarias para ejecutar el proyecto.

### `.gitignore`

Contiene los archivos y carpetas que no deben ser enviados al repositorio, como el entorno virtual y archivos temporales de Python.

## Base de datos MongoDB

Se utilizó MongoDB como sistema de almacenamiento de los datos.

Base de datos:

```text
taller3_db
```

Colección:

```text
raw_data
```

Los documentos almacenados contienen la información original obtenida desde la API.

Cada documento utiliza una estructura similar a:

```text
_id
resource_type
raw
```

Dentro de `raw` se encuentran los datos del personaje.

## Análisis exploratorio

El análisis se realizó utilizando Pandas y Jupyter Notebook.

Se seleccionaron siete variables principales:

```text
name
race
gender
ki
maxKi
affiliation
description
```

También se realizó una transformación de los valores de `ki` y `maxKi` para convertir los valores almacenados como texto en valores numéricos cuando fue posible.

## Insights obtenidos

El análisis permitió estudiar la distribución de los personajes según diferentes características.

Entre los resultados obtenidos se analizaron:

1. Cantidad total de personajes.
2. Distribución de personajes por género.
3. Afiliación con mayor cantidad de personajes.
4. Raza con mayor cantidad de personajes.
5. Valores de Ki disponibles, incluyendo promedio, máximo, mínimo y valores desconocidos.

Además, se encontró que la afiliación con mayor representación fue **Z Fighter**, con 19 personajes, seguida de **Other**, con 18 personajes.

La distribución de afiliaciones fue:

| Afiliación | Cantidad | Porcentaje |
|---|---:|---:|
| Z Fighter | 19 | 32.76% |
| Other | 18 | 31.03% |
| Villain | 9 | 15.52% |
| Army of Frieza | 5 | 8.62% |
| Pride Troopers | 4 | 6.90% |
| Freelancer | 1 | 1.72% |
| Assistant of Beerus | 1 | 1.72% |
| Assistant of Vermoud | 1 | 1.72% |

## Visualizaciones

El notebook contiene tres visualizaciones:

### 1. Gráfico de torta

Muestra la proporción de personajes según su género.

### 2. Gráfico de barras

Muestra la cantidad de personajes pertenecientes a cada afiliación.

### 3. Histograma

Muestra la distribución de los niveles de Ki de los personajes cuyos valores pudieron convertirse a números.

## Requisitos

Para ejecutar el proyecto se necesita:

- Python 3.10 o superior.
- MongoDB instalado y ejecutándose localmente.
- Jupyter Notebook o JupyterLab.
- Las librerías especificadas en `requirements.txt`.

## Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar a la carpeta:

```bash
cd proyecto_taller3
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Primero se debe tener MongoDB ejecutándose.

Después se ejecuta el script de ingesta:

```bash
python ingesta.py
```

Este proceso obtiene los datos de la API y los almacena en MongoDB.

Posteriormente se abre el notebook:

```bash
jupyter notebook
```

y se ejecuta:

```text
analisis.ipynb
```

Las celdas deben ejecutarse en orden para realizar correctamente la conexión, lectura, procesamiento, análisis y visualización de los datos.

## Repositorio

Repositorio público de GitHub:

**[PEGAR AQUÍ EL ENLACE DE TU REPOSITORIO]**

## Autor

**EMANUEL ALZATE**

Proyecto realizado para la asignatura **Bases de Datos para Ciencia de Datos**.