#!/usr/bin/python3
''' Class BaseModel '''

import uuid
from datetime import datetime


class BaseModel:
    '''
    Clase base que define todos los
    atributos / métodos comunes para otras clases
    '''
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            # Recorre la clave y valor en los items ingresados
            for key, value in kwargs.items():
                # Asigna la clave a la fecha actual de creación
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                # Asigna la clave a la fecha actualizada
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                # Se asigna el valor al key
                # self: Objeto cuyo atributo se va a asignar.
                # key: atributo del objeto que debe asignarse.
                # value: valor con el que se asignará la variable.
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            # Asigna id aleatorio
            self.id = str(uuid.uuid4)
            # Asigna fecha actual
            self.created_at = datetime.now().isoformat()
            # Actualiza la fecha de la ultima modificación
            self.updated_at = self.created_at

    def __str__(self):
        ''' devuelve el nombre de la clase, el ID y
        el diccionario de atributos '''
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dic__))

    def save(self):
        ''' actualiza el atributo de instancia pública
        updated_at con la fecha y hora actual '''
        self.updated_at = datatime.now().isoformat()

    def to_dict(self):
        ''' devuelve un diccionario que contiene todas
        las claves / valores de __dict__ de la instancia '''
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
