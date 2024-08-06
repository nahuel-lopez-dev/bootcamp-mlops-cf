<section id="inicio" align="center">
    <h1>Proyecto Final</h1>
    <h2 align="center">Bootcamp de MLOps</h2>
    <img width=500 src="./images/MLOps.png"/>
</section>

<h3>Proyecto para el Bootcamp de MLOps en <a href="https://codigofacilito.com">Código Facilito</a></h3>

<h3>Líder del bootcamp: <a href="https://www.linkedin.com/in/antonioferegrino/">Antonio Feregrino, Senior MLOps Engineer at simply Business</a></h3>

<h3>Tabla de Contenidos:</h3>

- [**Información del proyecto**](#información-del-proyecto) 📁
- [**Version 1.0.0**](#version-100) ✅
- [**Fuentes de datos**](#fuentes-de-datos) 🗄️
- [**Prerrequisitos**](#prerrequisitos) 📝
- [**Herramientas y tecnologías**](#herramientas-y-tecnologías) 🛠️
- [**Instalación y configuración del Entorno**](#instalación-y-configuración-del-entorno) 💻
- [**Desarrollo**](#desarrollo) ⚙️
- [**Screenshots**](#screenshots) 📸
- [**Información adicional**](#información-adicional) 🪧
- [**Agradecimientos**](#agradecimientos) 👋🏽
- [**Autores**](#autores) ⚡🪪

### **Información del proyecto**

Proyecto final para el bootcamp de MLOps de [Código Facilito](https://codigofacilito.com), donde se va a construir un ...

- Objetivo General:
  
  Construir un sistema de ETL donde se ingesta en una tabla de Snowflake la información de las ligas de fútbol más importantes de Europa

- Requisitos Específicos:
  - Extraer datos de múltiples fuentes (páginas web) con python.
  - Transformar estos datos con Python para obtener un dataset limpio.
  - Crear un DAG en Airflow, desplegado de manera local con Astro CLI, para que dos veces por semana vaya a la página web, extraiga la información, la transforme, y luego se cargue en una tabla en Snowflake.
  - Una vez hecho esto, se podrá hacer todo tipo de trabajos de analítica de datos, ya sea top five de los equipos con más goles, con menos goles, con mayor partidos ganados, etc.

- Alcance:
  
  Para el público en general, no se busca resolver una problemática en particular, sino practicar algunas de las herramientas vistas en el bootcamp para mostrar el desarrollo y despliegue a producción de un modelo de ML.


### **Version 1.0.0**

[![Demo](https://img.shields.io/badge/Demo_(En_proceso)-informational?style=for-the-badge&logo=vercel&logoColor=fff&color=23272d)](https://github.com/Nahuel-DevOne/data-engineering-cf)

### **Fuentes de datos**

- df_ligas.csv
- team_table.csv

### **Prerrequisitos**

Lista de software y herramientas, que necesitas para instalar y ejecutar este proyecto:

- WSL
- Git
- GitHub
- Docker
- Python
- Snowflake
- Airflow
- Astro CLI

### **Herramientas y tecnologías**

Tecnologías utilizadas para construir el proyecto:

- [Git](https://git-scm.com/) - El controlador de versiones utilizado
- [GitHub](https://github.com/) - La plataforma de desarrollo colaborativo, donde se aloja este proyecto.
- [Docker](https://www.docker.com/) - La tecnología de contenedores utilizada para manejar una imagen de airflow.
- [Python](https://www.python.org/) - El lenguaje de programación utilizado.
- [Pandas](https://pandas.pydata.org/) - Una librería  de Python para la manipulación y el análisis de los datos.
- [SQL](https://www.postgresql.org) - El lenguaje de consulta utilizado para bases de datos relacionales.
- [Snowflake](https://www.snowflake.com/es/) - La plataforma de almacenamiento de datos basada en la nube que fue utilizada. 
- [Airflow](https://airflow.apache.org/) - La plataforma de gestión de flujo (un orquestador) utilizada.
- [Astronomer](https://docs.astronomer.io/) - Aplicación de software como servicio (SaaS) que posee y ejecuta recursos de Astro. En este caso se utiliza Astro CLI para desplegar y correr la UI de Airflow.

### **Instalación y configuración del Entorno** 

Instalaciones y configuraciones del entorno

`Python`

Instalar Python: [Instalación](https://www.python.org/downloads/)

```bash
# Instalar según tu sistema operativo
```

`WSL`

Instalar WSL: [Instalación](https://learn.microsoft.com/es-es/windows/wsl/install)

```bash
# Por terminal
wsl --update
wsl.exe --install
```

`Docker`

Instalar Docker: [Instalación](https://www.docker.com/)

```bash
Seguir los pasos de instalación según tu sistema operativo.
Requiere de WSL para Windows
```

`Astro CLI`

```bash
# Instalar Astro CLI por medio de WSL
curl -sSL install.astronomer.io | sudo bash -s

# En el Visual Studio Code o el editor de tu preferencia, inicializar Astro y todos los paquetes necesarios
astro dev init

# Levantar la UI de Airflow
astro dev start o bien sudo astro dev start en caso de acceso denegado  
```

`Snowflake`

Crear cuenta en: [Snowflake](https://www.snowflake.com/es/)

```python
# Diseño del Modelo de Datos | Esquema de Snowflake:

# 1. Nombre de las configuraciones iniciales

Datawarehouse = normal_wh

Database = leagues

Stage = demo_stage

# 2. Crear un nuevo Worksheet desde la UI de Snowflake

# 3. Aplicar las siguientes queries desde tu Worksheet para crear tu DWH , DB y STAGE

# SET UP DWH , DATABASE and STAGE
 
CREATE or REPLACE warehouse normal_wh warehouse_size=XSMALL initially_suspended=true;
CREATE DATABASE leagues; 
CREATE STAGE "LEAGUES"."PUBLIC".demo_stage;

# 4. Crear una nueva tabla para recibir los datos de cada liga

# CREATE NEW TABLE
 
CREATE OR REPLACE TABLE football_leagues (
id         VARCHAR (30) NOT NULL,
equipo     VARCHAR (30) NOT NULL,
Jugados    INTEGER NOT NULL,
ganados    INTEGER NOT NULL,
empatados  INTEGER NOT NULL,
perdidos   INTEGER NOT NULL,
gf         INTEGER NOT NULL,
gc         INTEGER NOT NULL,
diff       INTEGER NOT NULL,
puntos     INTEGER NOT NULL,
liga       VARCHAR (30) NOT NULL,
created_at VARCHAR (30) NOT NULL
);

```

`Airflow`

Corre con una imagen de Docker que se levanta y ejecuta con Astro CLI

```bash
Se debe realizar la configuración de conexión con Snowflake y se generan las variables de entorno para proteger los datos sensibles de la misma.
A su vez, se configura la automatización, para repetir el proceso de ETL algunas veces en la semana.
```

---

### **Desarrollo**

`Extracción de Datos`

Utilizando Python y la librería de Pandas, se genera un dataframe con los datos de las ligas de Europa, usandola URL de cada liga y de su respectivo país.
De esta manera, se extraen los datos en un notebook de forma que luego se pueden trabajar para ser transformados.
 
`Transformación de Datos`

Ya cargado el dataframe, con los datos en crudo, se limpian y se transforman en datos útiles con Python y Pandas.
Se realiza un proceso llamado feature Engineering (o ingeniería de variables) para dejarlos datos en el formato que se necesitan para ser cargados.

`Carga de Datos`

Se trabaja en el almacén de los datos, Snowflake. Para ello se crea el stage (que es un área de almacenamiento temporal para archivos de datos antes de cargarlos en tablas) donde se pasa la base de datos con sus esquemas. Luego se crea la tabla de fútbol “football_leagues” (pasos detallados en la configuración). 
En este punto Airflow está funcional y listo para conectarse con Snowflake. 

`Funciones para extracción y transformación`

```python
import pandas as pd
import time
import random
import os
from datetime import datetime

def get_data(url,liga):
    
    tiempo = [1,3,2]
    time.sleep(random.choice(tiempo)) # para no recargar el servidor
    df = pd.read_html(url)
    df=pd.concat([df[0],df[1]],ignore_index=True,axis=1)
    df=df.rename(columns={0:'EQUIPO',1:'J', 2:'G', 3:'E', 4:'P', 5:'GF', 6:'GC', 7:'DIF', 8:'PTS'})
    df['EQUIPO']=df['EQUIPO'].apply(lambda x: x[5:] if x[:2].isnumeric()==True else x[4:])
    df['LIGA'] = liga

    # Obtener la hora de extracción
    run_date = datetime.now()
    run_date = run_date.strftime("%Y-%m-%d")
    df['CREATED_AT'] = run_date

    return df

def data_processing(df):

    df_spain=get_data(df['URL'][0],df['LIGA'][0])
    df_premier=get_data(df['URL'][1],df['LIGA'][1])
    df_italy=get_data(df['URL'][2],df['LIGA'][2])
    df_germany=get_data(df['URL'][3],df['LIGA'][3])
    df_francia=get_data(df['URL'][4],df['LIGA'][4])
    df_portugal=get_data(df['URL'][5],df['LIGA'][5])
    df_holanda=get_data(df['URL'][6],df['LIGA'][6])

    df_final=pd.concat([df_spain,df_premier,df_italy,df_francia,df_portugal,df_holanda],ignore_index=False)

    return df_final

```
Al finalizar el proceso de ETL, quedan cargados en una tabla de Snowflake todos los datos limpios y transformados listos para ser utilizados.
La ventaja de estar usando Airflow para orquestar el proceso, es que este trabajo queda automatizado y los datos en Snowflake van a ser actualizados periódicamente, según como se haya configurado. Esto se supone fundamental, en un contexto donde es necesario contar con los datos los más actualizados posibles, muchas veces para informes y toma de decisiones.


---

### **Screenshots**

En proceso...

---

### **Información adicional**

No es la intención de este proyecto resolver una problemática en específico, sino que el fin es mostrar como se podría hacer el despliegue a producción de un modelo de ML, llevando a cabo las mejores practicas de MLOps, utilizando varias de las herramientas y tecnologías vistas en el bootcamp, mostrando la vital importancia del rol de un MLOps dentro de un equipo de data.

---

### **Agradecimientos**

- En especial, agradecimiento a Código Facilito por la excelente experiencia del bootcamp, la entrega y el compromiso permanente con toda su comunidad, que se extiende más allá del ámbito académico y son un ejemplo de plataforma educativa a nivel internacional.
- Agradecimientos al líder del bootcamp Antonio Feregrino por diseñar los contenidos, y a todos los profesores y el equipo que conforman Código facilito, brindando su apoyo y conocimiento para lograr la mejor experiencia educativa.

---

### **Autores**

<p align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=21&pause=1000&color=C2D9F8&width=435&lines=¡Hola+mundo!+Soy+Nahuel.;Un+apasionado+Data+Engineer;y+Python+Developer⚡." alt="Typing SVG" /></a>
</p>

<h3>¡Hola, mi nombre es <b>Nahuel</b> 👋🏽!</h3>

- Soy de Buenos Aires (Argentina).
- Estudio Ingeniería en sistemas.
- Me gusta leer y estudiar sobre diversos temas, explorar nuevas tecnologías y resolver problemas.
- Me desempeño como Data Engineer en NTT Data, pero en mi trabajo diario hago tanto ingeniería de datos como ciencia de datos y machine learning.
- También tengo formación en desarrollo full Stack con JavaScript y Python.

💬 Siéntete libre de ponerte en contacto conmigo.

[![Contact Me](https://img.shields.io/badge/Gmail-informational?style=for-the-badge&logo=Mail.Ru&logoColor=fff&color=c6362c)](mailto:nahue.developer1@gmail.com)
[![LinkedId](https://img.shields.io/badge/LinkedIn-informational?style=for-the-badge&logo=linkedin&logoColor=fff&color=0274b3)](https://www.linkedin.com/in/nahuel-developer/)
[![GitHub Profile](https://img.shields.io/badge/GitHub-informational?style=for-the-badge&logo=GitHub&logoColor=fff&color=343941)](https://github.com/Nahuel-DevOne)
[![Linktree](https://img.shields.io/badge/-Linktree-323330?style=for-the-badge&logo=linktree&logoColor=#41e45f)](https://linktr.ee/nahuel.lopez)

<br>

<p align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=21&pause=1000&color=C2D9F8&width=435&lines=¡Hola+mundo!+Soy+Gabriel.;Un+apasionado+Data+Scientist;y+Geofísico⚡." alt="Typing SVG" /></a>
</p>

<h3>¡Hola, mi nombre es <b>Gabriel</b> 👋🏽!</h3>

- Soy de ...
- Estoy haciendo un doctorado en ...
- ...
- Me desempeño como Data Scientist en NTT Data ...
- También tengo formación en ...

💬 Siéntete libre de ponerte en contacto conmigo.

[![Contact Me](https://img.shields.io/badge/Gmail-informational?style=for-the-badge&logo=Mail.Ru&logoColor=fff&color=c6362c)](mailto:nahue.developer1@gmail.com)
[![LinkedId](https://img.shields.io/badge/LinkedIn-informational?style=for-the-badge&logo=linkedin&logoColor=fff&color=0274b3)](https://www.linkedin.com/in/nahuel-developer/)
[![GitHub Profile](https://img.shields.io/badge/GitHub-informational?style=for-the-badge&logo=GitHub&logoColor=fff&color=343941)](https://github.com/Nahuel-DevOne)
[![Linktree](https://img.shields.io/badge/-Linktree-323330?style=for-the-badge&logo=linktree&logoColor=#41e45f)](https://linktr.ee/nahuel.lopez)

Desarrollado con 💙 por [**Nahuel, Data Engineer**](https://linktr.ee/nahuel.lopez) y [**Gabriel Gelpi, Data Scientist**](https://linktr.ee/nahuel.lopez).

[**⚡Ir al inicio⚡**](#inicio)

---

