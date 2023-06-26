alumnos = []
def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    dni = input ("Ingre el DNI del estudiante: ")


    notas_practicos = []
    for i in range(6):
        nota = float(input(f"Ingrese la nota del trabajo practico {i+1}: "))
        notas_practicos.append(nota)

    nota_final = float(input("Ingrese la nota final(desaprobado o aprobado): "))
    promedio = sum(notas_practicos) / len(notas_practicos)

    estudiante = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "notas_practicos": notas_practicos,
        "promedio": promedio
    }    

    alumnos.append(estudiante)

    print("Estudiante agregado con éxito.")


    
def mostrar_aprobados_desaprobados():
    aprobados = []
    desaprobados = []

    for estudiante in alumnos:
        promedio = estudiante["promedio"]
        if nota_final >= 4.0
            aprobados.append((estudiante["nombre"], estudiante["apellido"]))
        else:
            desaprobados.append((estudiante["nombre"], estudiante["apellido"]))

    print("Estudiantes aprobados: ")
    for estudiante in aprobados
        print(f"{estudiante[0]} {estudiante[1]}")
    
    print("\nEstudiantes desaprobados: ")
    for estudiante in desaprobados:
        print(f"{estudiante[0]} {estudiante[1]}")



#Menu Principal
opcion = ""
while opcion!= "3:
    print("\n--- MENÚ ---")
    print("1. Agregar estudiante")
    print("2. Mostra estudiantes aprobados y desaprobados")
    print("3. SALIR")

    opcion = input("\nIngrese una opción: ")
    
    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        mostrar_aprobados_desaprobados()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")