# api-actividad_2
Los estudiantes deberán crear una API utilizando el framework Flask en Python. La API debe proporcionar un endpoint que devuelva una lista de nombres de personasLos estudiantes deberán implementar la lógica necesaria para generar esta lista y exponerla a través de la API.

Breve descripción de la API: 
La API "actividad2.py" es una aplicación web que devuelve una lista de nombres de personas en formato JSON. La API utiliza el framework Flask de Python y se ejecuta en un servidor local.

Instrucciones para ejecutar la API:
Clona el repositorio de GitHub utilizando el comando git clone https://github.com/orozco21/api-actividad_2.git
Abre una terminal y navega al directorio del proyecto utilizando el comando cd actividad2
Instala las dependencias necesarias utilizando el comando pip install -r requirements.txt
Ejecuta la API utilizando el comando python app.py
La API estará disponible en http://localhost:5000/nombres

Información sobre cómo utilizar la API
Para utilizar la API, simplemente envía una solicitud GET a la URL http://localhost:5000/nombres. La API devolverá una lista de nombres en formato JSON.
Ejemplo de solicitud utilizando cURL:

Bash
curl http://localhost:5000/nombres

Ejemplo de respuesta:
JSON
[
    "Juan Pablo Gastelbondo",
    "Juan Arrieta afanador",
    "Jonatan romero Fandiño",
    "Adrian Manuel Sanchez",
    "Casandra andrea molina",
    "Enrique orozco perez"
]
