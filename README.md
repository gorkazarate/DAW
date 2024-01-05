<!-- no toc -->

[![Generic badge](https://img.shields.io/badge/Python-3.8.12-blue.svg)](https://www.python.org/downloads/release/python-3812/)
[![Generic badge](https://img.shields.io/badge/NodeJS-16.13.0-green.svg)](https://nodejs.org/ko/blog/release/v16.13.0/)
[![Generic badge](https://img.shields.io/badge/NPM-8.1.3-darkred.svg)](https://libraries.io/npm/npm)
[![Generic badge](https://img.shields.io/badge/MongoDB_Server-4.4-darkgreen.svg)](https://www.mongodb.com/try/download/community)
[![Generic badge](https://img.shields.io/badge/OpenAPI-3.0.1-lightgreen.svg)](https://www.mongodb.com/try/download/community)

![demo_gif](./imgs/demo.gif)

## 1. Software necesario
- Python >=3.6 &emsp;&emsp;&emsp;&emsp;✅ 3.8.12
- NodeJS >= 10.6 &emsp;&emsp;&emsp;✅ 16.13.0
- NPM >= 6.10.0 &emsp;&emsp;&emsp;&nbsp;✅ 8.1.3
- MongoDB Server 4.4&emsp;&nbsp;✅ 4.4.10
- MySQL Community Server 8.2&emsp;&nbsp;✅ 8.2.0
   



## 2. Servicios a ejecutar
- Inicializar el servidor de MongoDB en el puerto 27017 (default).
- Desde la sección 'API y servicios > [Credentials](https://console.developers.google.com/apis/credentials)' de Google Cloud Platform tenemos que generar 1 nueva credencial:
  * ID de cliente OAuth 2.0: Utilizado por el OAuth server para permitir el OAuth login de Google, en este caso se generarán el ID de cliente [GOOGLE_CLIENT_ID] y el Secreto del cliente [GOOGLE_CLIENT_SECRET]. Al generar esta credencial establecemos las siguientes opciones:
    - Tipo de aplicación: Aplicación web.
    - URI de redireccionamiento autorizado: 'http://127.0.0.1:8000' y 'http://127.0.0.1:9090/auth/google/callback'.
  - Rellenamos el fichero keys.json del directorio raíz con las claves API y Secret generados.



## 3. Dependencias a instalar
En primer lugar, tras instalar NodedJS y NPM nos ubicaremos en el directorio /OAuth_server y ejecutamos el siguiente comando:
```
npm install
```
## 4. Como arrancar la parte servidora
Para inicializar al completo la parte servidora, tendremos que inicializar cada uno de los microservicios, por un lado nos ubicamos en el directorio /publicaciones y ejecutamos el siguiente comando:
```
python main.py
```
Por otro lado, ejecutamos el servidor que se encarga del OAuth y hace de Gateway al microservicio Publicaciones server. Nos ubicamos en el directorio /OAuth_api y ejecutamos el comando:
```
node index.js 