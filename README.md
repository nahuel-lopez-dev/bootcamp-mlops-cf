<section id="inicio" align="center">
    <h1>Proyecto Final</h1>
    <h2 align="center">Bootcamp de MLOps</h2>
    <img width=500 src="./images/MLOps.png"/>
</section>

<h3>Proyecto final para el Bootcamp de MLOps en <a href="https://codigofacilito.com">Código Facilito</a></h3>

<h3>Líder del bootcamp: <a href="https://www.linkedin.com/in/antonioferegrino/">Antonio Feregrino, Senior MLOps Engineer at simply Business</a></h3>

<h3>Tabla de Contenidos:</h3>

- [**Información del proyecto**](#información-del-proyecto) 📁
  
- [**Version 1.0.0**](#version-100) ✅
  
- [**Fuentes de datos**](#fuentes-de-datos) 🗄️
  
- [**Prerrequisitos**](#prerrequisitos) 📝
  
- [**Herramientas y tecnologías**](#herramientas-y-tecnologías) 🛠️
  
- [**Instalación y configuración del Entorno**](#instalación-y-configuración-del-entorno) 💻
  
- [**Desarrollo**](#desarrollo) ⚙️
  - [Procesos](#procesos)
    - [1. Proceso1](#1-proceso1)
    - [2. Proceso2](#2-proceso2)
    - [3. Proceso3](#3-proceso3)
  
- [**Screenshots**](#screenshots) 📸

- [**Información adicional**](#información-adicional) 🪧

- [**Agradecimientos**](#agradecimientos) 👋🏽

- [**Autores**](#autores) 🪪

## **Información del proyecto**

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


## **Version 1.0.0**

[![Demo](https://img.shields.io/badge/Demo_(En_proceso)-informational?style=for-the-badge&logo=vercel&logoColor=fff&color=23272d)](https://github.com/Nahuel-DevOne/data-engineering-cf)

## **Fuentes de datos**

- df_ligas.csv
- team_table.csv

## **Prerrequisitos**

Lista de software y herramientas, que necesitas para instalar y ejecutar este proyecto:

- WSL
- Git
- GitHub
- Docker
- Python
- Snowflake
- Airflow
- Astro CLI

## **Herramientas y tecnologías**

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

## **Instalación y configuración del Entorno** 

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


`Airflow`

Corre con una imagen de Docker que se levanta y ejecuta con Astro CLI

```bash
Se debe realizar la configuración de conexión con Snowflake y se generan las variables de entorno para proteger los datos sensibles de la misma.
A su vez, se configura la automatización, para repetir el proceso de ETL algunas veces en la semana.
```

## **Desarrollo**

Para desarrollar este proyecto se utiliza...

### Procesos

#### 1. Proceso1
   
   - dfafaf
   - fdasf
   - dfafa
   - dfafadf
   - dfafafd
   - dfafd
   - 
   
#### 2. Proceso2
    
   - dfafaf
   - dfadf
   - dfadfa
   - dfdfaf
   - dfadf
 
#### 3. Proceso3

   - dfafaf
   - dfadf
   - dfadfa
   - dfdfaf
   - dfadf

## **Screenshots**

En proceso...


## **Información adicional**

No es la intención de este proyecto resolver una problemática en específico, sino que el fin es mostrar como se podría hacer el despliegue a producción de un modelo de ML, llevando a cabo las mejores practicas de MLOps, utilizando varias de las herramientas y tecnologías vistas en el bootcamp, mostrando la vital importancia del rol de un MLOps dentro de un equipo de data.


## **Agradecimientos**

- En especial, agradecimiento a Código Facilito por la excelente experiencia del bootcamp, la entrega y el compromiso permanente con toda su comunidad, que se extiende más allá del ámbito académico y son un ejemplo de plataforma educativa a nivel internacional.
- Agradecimientos al líder del bootcamp Antonio Feregrino por diseñar los contenidos, y a todos los profesores y el equipo que conforman Código facilito, brindando su apoyo y conocimiento para lograr la mejor experiencia educativa.

## **Autores**

<p align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=21&pause=1000&color=C2D9F8&width=435&lines=¡Hola+mundo!+Soy+Nahuel.;Un+apasionado+Data+Engineer;y+Python+Developer⚡." alt="Typing SVG" /></a>
</p>

<div>
  <h3>¡Hola, mi nombre es <b><i>Nahuel</i></b> 👋🏽!! <br></h3>
  <p>Soy de Buenos Aires (Argentina) y tengo formación en desarrollo con Python, Ingeniería y Ciencia de Datos. Me desempeño como Data Engineer, aunque en mi trabajo diario hago tanto ingeniería de datos como ciencia de datos, machine learning y desarrollo con Python.
  <br>Amo el mundo de los datos pero también el desarrollo. Actualmente, estudio Ingeniería en Sistemas, y en mis momentos libres dedico gran parte de mi tiempo a seguir aprendiendo nuevas tecnologías, como así también a practicar y reforzar mi stack como Ingeniero de Datos.</p>
</div>

Si quieres saber más sobre mí, puedes ir a mi perfil de GitHub:

[![GitHub Profile](https://img.shields.io/badge/GitHub:-Nahuel_Lopez_Dev_ထ-05122A?flat&logo=github&logoColor=white&labelColor=343941)](https://github.com/nahuel-lopez-dev)
  
💬 Siéntete libre de ponerte en contacto conmigo:

[![Contact Me](https://img.shields.io/badge/Gmail-informational?flat&logo=Mail.Ru&logoColor=fff&color=c6362c)](mailto:nahuel.developer1@gmail.com)&nbsp;
[![LinkedId](https://img.shields.io/badge/LinkedIn-informational?flat&logo=linkedin&logoColor=fff&color=0274b3)](https://www.linkedin.com/in/nahuel-developer/)&nbsp;
[![Linktree](https://img.shields.io/badge/-Linktree-323330?flat&logo=linktree&logoColor=#41e45f)](https://linktr.ee/nahuel.lopez)

<br>

<p align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=21&pause=1000&color=C2D9F8&width=435&lines=¡Hola+mundo!+Soy+Gabriel.;Un+apasionado+Data+Scientist;y+Geofísico⚡." alt="Typing SVG" /></a>
</p>

<div>
  <h3>¡Hola, mi nombre es <b><i>Gabriel</i></b> 👋🏽!! <br></h3>
  <p>Soy de ... y tengo formación en
  <br>Otra información...</p>
</div>

Si quieres saber más sobre mí, puedes ir a mi perfil de GitHub:

[![GitHub Profile](https://img.shields.io/badge/GitHub:-Nahuel_Lopez_Dev_ထ-05122A?flat&logo=github&logoColor=white&labelColor=343941)](https://github.com/nahuel-lopez-dev)
  
💬 Siéntete libre de ponerte en contacto conmigo:

[![Contact Me](https://img.shields.io/badge/Gmail-informational?flat&logo=Mail.Ru&logoColor=fff&color=c6362c)](mailto:nahuel.developer1@gmail.com)&nbsp;
[![LinkedId](https://img.shields.io/badge/LinkedIn-informational?flat&logo=linkedin&logoColor=fff&color=0274b3)](https://www.linkedin.com/in/nahuel-developer/)&nbsp;
[![Linktree](https://img.shields.io/badge/-Linktree-323330?flat&logo=linktree&logoColor=#41e45f)](https://linktr.ee/nahuel.lopez)

<br>

Desarrollado con 💙 por [**Nahuel, Data Engineer**](https://linktr.ee/nahuel.lopez) y [**Gabriel Gelpi, Data Scientist**](https://linktr.ee/nahuel.lopez).

[**⚡Ir al inicio⚡**](#inicio)

<img src="https://capsule-render.vercel.app/api?type=waving&color=C2D9F8&height=80"/>

