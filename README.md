# Api de Recolección de Mazos

![](https://img.shields.io/badge/Notepad++-90E59A.svg?style=for-the-badge&logo=notepad%2B%2B&logoColor=black) ![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white) ![](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white) ![](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white)


## Objetivo 👈
Hacer una api para mostrar una base de datos NoSQL y poder manipularlo para análisis sobre mazos usados por la comunidad hispanohablante en el videojuego Yu-Gi-Oh!Duel Links.

## Estructura del Proyecto 📦

    ├── db                 <- Almacena los parámetros de la base de datos.
	│   ├── models
	│   │    └── users.py
	│   │
    │   ├── schemas
	│   │    └── user.py
	│   │
    │   ├── client.py      <- Archivo para la conexión de base de datos
	│   └── .env		   <- Complemento del client.py
	│
	├── routers            <- Carpeta para segmentar los torneos
	│   └── fecha-del-torneo.py
	│
	├── .gitignore         <- Ignorar carpetas caché y el .env
    ├── main.py            <- Inicio de la API y almacén de routers.
	├── README.md          <- La guía del proyecto.
    └── requirements.txt   <- Librerías del proyecto.

## Visualización de la API ⚙️
![](https://i.pinimg.com/originals/a0/7b/c5/a07bc58457f0361635cb8d9a24abfc6c.gif)

| Columna | Tipo de Dato |Descripción | 
| :---: | :---: | :---: | 
| id | String | Id característico de registro en MongoDB |
| duelist | Integer | Código identificatorio universal del usuario |
| deck | String | El mazo usado |
| skill | String | La habilidad usada para el deck |
| zerotg | Boolean | Usuario perteneciente a la comunidad descripta |
| zephra | Boolean | Usuario perteneciente a la comunidad descripta |
| bryan | Boolean | Usuario perteneciente a la comunidad descripta |
| ndmax | String | Fecha que llegó al rango máximo del torneo |

## Enlaces de interés
* Proyecto basado al [curso de Python desde Cero para Backend por MoureDev by Brais Moure](https://youtu.be/_y9qQZXE24A)
* [La Guía del curso de Python desde cero de MoureDev](https://github.com/mouredev/Hello-Python)
* La framework para crear APIs [FastAPI](https://fastapi.tiangolo.com/es/)
* La base de datos [MongoDB](https://www.mongodb.com/)
* El desplegue de la API en la nube gracias al sponsor de FastAPI, [Deta](https://deta.space/from-cloud)
* Software para usar la API, [Postman](https://www.postman.com)
* [El Videojuego Yu-Gi-Oh! Duel Links](https://www.konami.com/yugioh/duel_links/en/)
* Los Creadores de Contenido del juego nombrados en la base de datos

	| Variable | Canal |
	| :---: | :---: |
	| zerotg | [ZeroTG](https://www.youtube.com/@ZeroTG) |
	| zephra | [ZephraCarl](https://www.youtube.com/@ZephraCarl) |
	| bryan | [Bryan Norén](https://www.youtube.com/@BryanNoren) |

## License 🧾
The MIT License (MIT)

![](https://i.pinimg.com/originals/00/d2/d2/00d2d2440c90766fedea7609bcb61cac.gif)