# Para correr el servidor, tenemos que estar seguros de estar en la raiz del proyecto y estar en nuestro entorno virtual con sus dependencias instaladas. El comando es el siguiente
    # uvicorn main:app --reload
    # main es el nombre del archivo, app es el nombre de la variable que contiene nuestra aplicacion y --reload es una bandera que reiniciara nuestro servidor cada vez que realicemos un cambio en el codigo (esto solo deberia de utilizarse en desarrollo)

from fastapi import FastAPI
import schemas # importamos nuestro archivo schemas.py

app = FastAPI()

fakeDatabase = {
    1: {'task': 'Clean car'},
    2: {'task': 'Write blog'},
    3: {'task': 'Start stream'},
}

# Mi primera ruta
@app.get('/')
def getItems():
    return fakeDatabase

# Path parameters
# Esta ruta espera un entero como parametro que representa el id de una tarea en nuestra base de datos ficticia. (para que no de errores, tenemos que asegurarnos de que el id indicado este disponible en nuestra base de datos)
@app.get('/{id}')
def getItem(id:int):
    return fakeDatabase[id]

# Peticiones POST, PUT and DELETE
# Una peticion POST es para aniadir datos.
# Una peticion PUT usualmente para actualizar datos.
# Una peticion DELETE para eliminar datos.

# Ruta con POST
# Aqui especificamos el tipo de peticion que recibira esta ruta.
@app.post('/')
# Aqui accedmemos a la clase Body y la aniadimos como parametro en nuestra ruta
def addItem(item:schemas.Item):
    newId = len(fakeDatabase.keys()) + 1
    # esto nos crea un diccionario al que accedemos mediante su 'indice nombrado'
    fakeDatabase[newId] = {'task': item.task}
    return fakeDatabase

# Actualizando datos
@app.put('/{id}')
def updateItem(id:int, item:schemas.Item):
    fakeDatabase[id]['task'] = item.task
    return fakeDatabase

# Borrando datos
@app.delete('/{id}')
def deleteItem(id:int):
    del fakeDatabase[id]
    return fakeDatabase