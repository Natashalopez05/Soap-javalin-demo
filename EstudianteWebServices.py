import zeep

cliente = zeep.Client(wsdl="http://localhost:7000/ws/EstudianteWebServices?wsdl")


def listar_estudiantes():
    return cliente.service.getListaEstudiante()

def buscar_estudiante(matricula):
    return cliente.service.getEstudiante(matricula)

def crear_estudiante(matricula, nombre, carrera):
    estudiante = {'matricula': matricula, 'nombre': nombre, 'carrera': carrera}
    return cliente.service.crearEstudiante(estudiante)

def borrar_estudiante(matricula):
    return cliente.service.borrarEstudiante(matricula)


if __name__ == "__main__":
    print("Lista de estudiantes:")
    print(listar_estudiantes())

    print("\nBuscar estudiante con matrícula:")
    print(buscar_estudiante(20011136))
    

    print("\nCrear nuevo estudiante:")
    nuevo_estudiante = crear_estudiante(10141277, "Juan", "ICC")
    nuevo_estudiante2 = crear_estudiante(10141896, "Pedro", "PM")
    nuevo_estudiante3 = crear_estudiante(10146058, "Maria", "COM")

    print("Estudiante creado:", nuevo_estudiante)
    print("Estudiante creado:", nuevo_estudiante2)
    print("Estudiante creado:", nuevo_estudiante3)


    print("\nBorrar estudiante con matricula:")
    print(borrar_estudiante(10141277))


