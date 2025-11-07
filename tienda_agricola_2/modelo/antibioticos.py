class Antibiotico:
    def __init__(self, nombre, precio,dosis,tipo_animal):

        self.__validar_animal(tipo_animal)
        self.__validar_dosis(dosis)

        self.__nombre_producto = nombre
        self.__precio = precio
        self.__dosis = dosis
        self.__tipo_animal = tipo_animal
    
    def __validar_dosis(self,dosis):
        if not (400 <= dosis <= 600):
            raise ValueError("La dosis debe estar entre 400Kg - 600Kg.")

    def __validar_animal(self,tipo_animal):
        tipos_validos = ["Bovinos","Porcinos","Caprinos"]

        if tipo_animal not in tipos_validos:
            raise ValueError(f"Tipo de animal incorrecto, debe ser: {tipos_validos[0]} ó {tipos_validos[1]} ó {tipos_validos[2]}")
    @property
    def nombre(self):
        return self.__nombre_producto

    @property
    def precio(self):
        return self.__precio

    @property
    def dosis(self):
        return self.__dosis
    
    @property
    def tipo_animal(self):
        return self.__tipo_animal
    
    def __str__(self):
        return f"""Nombre: {self.__nombre_producto} -- Precio: {self.__precio}
                Dosis: {self.__dosis} Kg -- Tipo animal: {self.__tipo_animal}"""
    
