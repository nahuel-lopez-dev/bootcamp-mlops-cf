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

Proyecto final para el bootcamp de MLOps de [Código Facilito](https://codigofacilito.com).

- Objetivo General:
  
  Construir una aplicación a partir de la cual se sube una imagen de un perro o gato y se tiene como resultado  el nombre del animal que aparece en la imagen. 

- Objetivos Específicos:
  - Extraer y cargar imagenes de gatos y perros, y almacenarlas de forma adecuada.
  - Entrenamiento de una red neuronal básica para realizar la clasificación.
  - Trackeo de la información necesaria del entrenamiento del modelo y correcto registro del mismo.
  - Despliegue del modelo de manera online.
  - Monitoreo del mismo y definicioes para el re entrenamiento del modelo.
  - Limitaciones y próximos pasos.

- Alcance:
  
  Proyecto end to end de MLOps para para un problema básico de computer vision como la clasificación de imagenes.

## **Version 1.0.0**

[![Demo](https://img.shields.io/badge/Demo_(En_proceso)-informational?style=for-the-badge&logo=vercel&logoColor=fff&color=23272d)](https://github.com/Nahuel-DevOne/data-engineering-cf)

## **Fuentes de datos**

- df_ligas.csv
- team_table.csv

## **Prerrequisitos**

Lista de software y herramientas, que necesitas para instalar y ejecutar este proyecto:

- Git
- GitHub
- Docker
- Python
- Flask
- Tensorflow

## **Herramientas y tecnologías**

Tecnologías utilizadas para construir el proyecto:

- [Git](https://git-scm.com/) - El controlador de versiones utilizado
- [GitHub](https://github.com/) - La plataforma de desarrollo colaborativo, donde se aloja este proyecto.
- [Docker](https://www.docker.com/) - La tecnología de contenedores utilizada para manejar una imagen de airflow.
- [Python](https://www.python.org/) - El lenguaje de programación utilizado.
- [Flask](https://pandas.pydata.org/) - Una librería  de Python para la manipulación y el análisis de los datos.
- [TensorFlow-Keras](https://www.postgresql.org) - El lenguaje de consulta utilizado para bases de datos relacionales.

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

Desde el punto de vista de Machine Learning el problema a resolver es un problema de clasificación binario para esta versión inicial. 
### Etapas

#### 1. Data
   
- Datasets: En páginas como Kaggle se pueden obtener datasets ya armados con imagenes como las que se utiliza para entrenar el modelo de Deep Learning. Particularmente para este proyecto se utilizó el dataset www.kaggle
.com/c/dogs-vs-cats/data . No obstante se podrían usar otros dataset y combinarlos para incrementar el número de datos.

- Imagenes personales: Luego si uno quisiera podría subir imagenes de sus mascotas personales, respetando el criterio en el que se separan las imagenes para los entrenamientos.

- Inferencia: El usuario debería de poder subir su imagen en formato JPG a la aplicación para ver que animal aparece. 
   

#### 2. Preprocesamiento

El entrenamiento requiere un número de pasos para poder llevar
 a cabo el modelo. El primero es llevar las imagenes, que se
 asume que tienen su etiquta coomo nombre, en tres carpetas distintas de train, test y validacion. Dentro de cada una de ellas se tiene una carpeta por clase (una para perros y otra para gatos). Además se debe de realizar un *resizing* de las imagenes y un escalamiento de los datos para poder alimentar el modelo deep learing. Este ultimo paso está como una capa mas dentro de la arquitectura de la red. 



#### 3. Modelo
    
 Para entrenar el modelo de clasificación se utilizó una red neuronal convolucional básica con 5 capas convolucionales. Se utilizó la libreria de tensorflow con Keras ya que tiene una buena documentación y es relativamente simple para implementar modelos de machine learning apilando capas. 
 Para tener control y poder de decisión sobre los modelos, experimentos y registro de modelos se utilizó la librería MLFlow. Dicha librería nos permite hacer un trackeo de cada una de las pruebas de entrenamiento mediante una UI y registrar modelos. Luego con la misma librería a través de su API se puede invocar los modelos para realizar las inferencias.



#### 3. Inferencia

Para esta aplicación el tipo de inferencia es de tipo Online. Esto es a demanda de un usuario, el cual sube una imagen a la aplicación y esta devuelve como resultado el nombre del animal y probabilidad con la que asegura la predicción. El servicio de inferencia se ofrece a través del framework web Flask por su simplicidad y capacidad de integración con otras herramientas. A través de MLFlow se comparan los modelos registrados y se utiliza como modelo productivo el que posee el alias de *Champion*. 


#### 5. CI/CD
La integración continua, despliegue y re entrenamiento del modelo se realiza con Github Actions. El disparador o *trigger* es al realizar un push al repo. Esto puede darse al actualizar las imagenes para mejorar y/o customizar el dataset y por ende las salidas del modelo. También al actualizar el modelo ya sea por una modificación del mismo o querer usar otro modelo. En esta situación la definición de modelo *champion* estará dada por la comparación de una métrica.



#### 6. Infra de Servicio
#### 7. Workflow y datos
#### 8. Interacción de usuarios
#### 9. Limitaciones



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
  <p>Platense viviendo en la ciudad de Buenos Aires (Argentina). Si bien me recibí de Geofísico, desde hace un tiempo trabajo como Data Scientist. Acualmente estoy involucrado en proyectos de series temporales y detección de anomalías. </p>  
</div>

Si quieres saber más sobre mí, puedes ir a mi perfil de GitHub:

[![GitHub Profile](https://img.shields.io/badge/GitHub:-Geofgabriel_ထ-05122A?flat&logo=github&logoColor=white&labelColor=343941)](https://github.com/Geofgabriel)
  
💬 Siéntete libre de ponerte en contacto conmigo:

[![Contact Me](https://img.shields.io/badge/Gmail-informational?flat&logo=Mail.Ru&logoColor=fff&color=c6362c)](mailto:nahuel.developer1@gmail.com)&nbsp;
[![LinkedId](https://img.shields.io/badge/LinkedIn-informational?flat&logo=linkedin&logoColor=fff&color=0274b3)](https://www.linkedin.com/in/nahuel-developer/)&nbsp;
[![Linktree](https://img.shields.io/badge/-Linktree-323330?flat&logo=linktree&logoColor=#41e45f)](https://linktr.ee/nahuel.lopez)

<br>

Desarrollado con 💙 por [**Nahuel, Data Engineer**](https://linktr.ee/nahuel.lopez) y [**Gabriel Gelpi, Data Scientist**](https://linktr.ee/nahuel.lopez).

[**⚡Ir al inicio⚡**](#inicio)

<img src="https://capsule-render.vercel.app/api?type=waving&color=C2D9F8&height=80"/>

