class Antibiotico:
    def __init__(self, nombre, precio,dosis,tipo_animal):

        self._validar_animal(tipo_animal)
        self._validar_dosis(dosis)

        self._nombre_producto = nombre
        self._precio = precio
        self._dosis = dosis
        self._tipo_animal = tipo_animal
    
    def _validar_dosis(self,dosis):
        if not (400 <= dosis <= 600):
            raise ValueError("La dosis debe estar entre 400Kg - 600Kg.")

    def _validar_animal(self,tipo_animal):
        tipos_validos = ["Bovinos","Porcinos","Caprinos"]

        if tipo_animal not in tipos_validos:
            raise ValueError(f"Tipo de animal incorrecto, debe ser: {tipos_validos[0]} ó {tipos_validos[1]} ó {tipos_validos[2]}")
    
    def get_nombre(self):
        return self._nombre_producto
    
    def get_precio(self):
        return self._precio

    def get_dosis(self):
        return self._dosis
    
    def get_tipo_animal(self):
        return self._tipo_animal

    def __str__(self):
        return f"""Nombre: {self._nombre_producto} -- Precio: {self._precio}
                Dosis: {self._dosis} Kg -- Tipo animal: {self._tipo_animal}"""
    
