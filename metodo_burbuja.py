class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza

        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo
        nuevo.anterior = actual

    def mostrar(self):
        actual = self.cabeza

        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente

        print("None")

    def burbuja(self):
        if self.cabeza is None:
            return

        cambiado = True

        while cambiado:
            cambiado = False
            actual = self.cabeza

            while actual.siguiente:
                if actual.dato > actual.siguiente.dato:
                    actual.dato, actual.siguiente.dato = actual.siguiente.dato, actual.dato
                    cambiado = True

                actual = actual.siguiente

    def buscar(self, valor):
        actual = self.cabeza
        posicion = 0

        while actual:
            if actual.dato == valor:
                return f"Encontrado en la posición {posicion}"

            actual = actual.siguiente
            posicion += 1

        return "No encontrado"


lista = ListaDoble()

lista.insertar(5)
lista.insertar(2)
lista.insertar(9)
lista.insertar(1)

print("Lista original:")
lista.mostrar()

lista.burbuja()

print("Lista ordenada:")
lista.mostrar()

print(lista.buscar(9))
print(lista.buscar(7))