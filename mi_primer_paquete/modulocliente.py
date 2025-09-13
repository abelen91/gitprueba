class Cliente:
    def __init__(self, nombre, email, domicilio, intereses):
        self.nombre = nombre
        self.email = email
        self.domicilio = domicilio
        self.intereses = intereses
        self.historial_compras = []  

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}, Domicilio {self.domicilio}, Intereses: {self.intereses}"

    # Método agregar compras
    def agregar_compra(self, producto):
        self.historial_compras.append(producto)

    # Método mostrar historial
    def mostrar_historial(self):
        if self.historial_compras:
            return f"Historial de compras: {', '.join(self.historial_compras)}"
        else:
            return "No tiene compras registradas"
        
