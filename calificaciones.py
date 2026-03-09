class Estudiante:
    """
    Representa a un estudiante con información académica básica.

    Atributos:
        identificacion (int): Número único que identifica al estudiante.
        nombre (str): Nombre completo del estudiante.
        semestre (str): Semestre actual que cursa el estudiante.
        calificaciones (list[float]): Lista de calificaciones obtenidas por el estudiante.
    """

    identificacion: int
    nombre: str
    semestre: str
    calificaciones: list[float]

    def __init__(self, identificacion: int, nombre: str, semestre: str, calificaciones: list[float]):
        self.identificacion = identificacion
        self.nombre = nombre
        self.semestre = semestre
        self.calificaciones = calificaciones

    def obtener_promedio(self):
        """
        Calcula y retorna el promedio de las calificaciones del estudiante.
        """
        if not self.calificaciones:
            raise ValueError("El estudiante no tiene calificaciones registradas.")
        return sum(self.calificaciones) / len(self.calificaciones)

    def ver_informacion(self):
        """
        Retorna la información general del estudiante en forma texto.
        """
        promedio = self.obtener_promedio() if self.calificaciones else 0.0 #se usaba el atributo "calificación", pero estaba definido antes como "calificaciones" en plural, por eso daba el error.
        return (
            f"ID: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Semestre: {self.semestre}\n"
            f"Promedio: {promedio:.2f}"
        )


# Lista de estudiantes
estudiantes: list[Estudiante] = []

while True:
    print("\n1. Agregar estudiante")
    print("2. Ver promedio estudiante")
    print("3. Ver información de un estudiante")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        identificacion = int(input("Ingrese la identificación del estudiante: "))
        nombre = input("Ingrese el nombre del estudiante: ")
        semestre = input("Ingrese el semestre del estudiante: ")

        print("Ingrese las calificaciones del estudiante")
        notas = []

        for i in range(3):
            nota = float(input(f"Calificación {i + 1}: "))
            notas.append(nota)

        estudiante = Estudiante(identificacion, nombre, semestre, notas)
        estudiantes.append(estudiante)

        print("Estudiante agregado correctamente.")

    elif opcion == "2" or opcion == "3":
        identificacion = int(input("Ingrese la identificación del estudiante: "))

        for estudiante in estudiantes:
            if estudiante.identificacion == identificacion and opcion == "2":
                print(f"\nEstudiante: {estudiante.nombre}")
                print(f"Promedio: {estudiante.obtener_promedio():.2f}")
                break

            elif estudiante.identificacion == identificacion and opcion == "3":
                print("\nInformación del estudiante:")
                print(estudiante.ver_informacion())
                break
        else:
            print("Estudiante no encontrado.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")