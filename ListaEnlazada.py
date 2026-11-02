class Nodo:
    def __init__(self, producto, precio, cantidad):
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad
        self.subtotal = precio * cantidad
        self.sig = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Comprobar si la lista está vacía
    def esta_vacia(self):
        return self.cabeza is None

    # Agregar producto al final de la lista
    def agregar(self, producto, precio, cantidad):
        nuevo = Nodo(producto, precio, cantidad)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza
        while actual.sig is not None:
            actual = actual.sig

        actual.sig = nuevo

    # Mostrar productos y total
    def mostrar(self):
        if self.cabeza is None:
            print("\nNo hay productos en la lista de compras.")
            return

        actual = self.cabeza
        total = 0

        print("\n========== LISTA DE COMPRAS ==========")
        while actual is not None:
            print(f"Producto: {actual.producto}")
            print(f"Precio unitario: ${actual.precio:.2f}")
            print(f"Cantidad: {actual.cantidad}")
            print(f"Subtotal: ${actual.subtotal:.2f}")
            print("--------------------------------------")
            total += actual.subtotal
            actual = actual.sig

        print(f"TOTAL DE LA COMPRA: ${total:.2f}")

    # Calcular el total de todos los productos
    def calcular_total(self):
        actual = self.cabeza
        total = 0

        while actual is not None:
            total += actual.subtotal
            actual = actual.sig

        return total
