
def agregar_usuario(usuarios):
    id_usuario = input("ID del usuario: ")
    nombre = input("Nombre del usuario: ")
    telefono = input("Telefono del usuario: ")
    rol = input("Rol del usuario: ")
    usuarios.append((id_usuario, nombre, telefono, rol, []))
    print("Usuario agregado.\n")


def ver_usuarios(usuarios):
    if not usuarios:
        print("No hay usuarios registrados.\n")
    else:
        print("---- LISTA DE USUARIOS ----")
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Telefono: {usuario[2]}, Rol: {usuario[3]}, Tareas: {len(usuario[4])}")
        print()


def actualizar_usuario(usuarios):
    id_usuario = input("ID del usuario a actualizar: ")
    for i, usuario in enumerate(usuarios):
        if usuario[0] == id_usuario:
            nuevo_nombre = input("Nuevo nombre (Enter para mantener): ")
            nuevo_telefono = input("Nuevo telefono (Enter para mantener): ")
            nuevo_rol = input("Nuevo rol (Enter para mantener): ")
            nombre = nuevo_nombre if nuevo_nombre else usuario[1]
            telefono = nuevo_telefono if nuevo_telefono else usuario[2]
            rol = nuevo_rol if nuevo_rol else usuario[3]
            usuarios[i] = (usuario[0], nombre, telefono, rol, usuario[4])
            print("Usuario actualizado.\n")
            return
    print("Usuario no encontrado.\n")


def eliminar_usuario(usuarios):
    id_usuario = input("ID del usuario a eliminar: ")
    for i, usuario in enumerate(usuarios):
        if usuario[0] == id_usuario:
            usuarios.pop(i)
            print("Usuario eliminado.\n")
            return
    print("Usuario no encontrado.\n")


def agregar_tarea(usuarios, id_usuario):
    for usuario in usuarios:
        if usuario[0] == id_usuario:
            id_tarea = input("ID de la tarea: ")
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            estado = input("Estado (Pendiente/Completada): ")
            usuario[4].append((id_tarea, titulo, descripcion, estado))
            print("Tarea agregada.\n")
            return
    print("Usuario no encontrado.\n")


def ver_tareas(usuarios, id_usuario):
    for usuario in usuarios:
        if usuario[0] == id_usuario:
            if not usuario[4]:
                print("No hay tareas registradas para este usuario.\n")
            else:
                print(f"---- TAREAS DE {usuario[1]} ----")
                for tarea in usuario[4]:
                    print(f"ID: {tarea[0]}, Título: {tarea[1]}, Descripción: {tarea[2]}, Estado: {tarea[3]}")
                print()
            return
    print("Usuario no encontrado.\n")
    
    
def total_tareas_por_estado(usuarios):
    pendientes = 0
    completadas = 0

    for usuario in usuarios:
        for tarea in usuario[4]:
            if tarea[3].lower() == "pendiente":
                pendientes += 1
            elif tarea[3].lower() == "completada":
                completadas += 1

    print("---- REPORTE TOTAL DE TAREAS ----")
    print(f"Tareas Pendientes: {pendientes}")
    print(f"Tareas Completadas: {completadas}\n")


def actualizar_tarea(usuarios, id_usuario):
    for i, usuario in enumerate(usuarios):
        if usuario[0] == id_usuario:
            if not usuario[4]:
                print("Este usuario no tiene tareas.\n")
                return
            id_tarea = input("ID de la tarea a actualizar: ")
            for a, tarea in enumerate(usuario[4]):
                if tarea[0] == id_tarea:
                    nuevo_titulo = input("Nuevo título (Enter para mantener): ")
                    nueva_desc = input("Nueva descripción (Enter para mantener): ")
                    nuevo_estado = input("Nuevo estado (Pendiente/Completada, Enter para mantener): ")
                    titulo = nuevo_titulo if nuevo_titulo else tarea[1]
                    desc = nueva_desc if nueva_desc else tarea[2]
                    estado = nuevo_estado if nuevo_estado else tarea[3]
                    usuario[4][a] = (tarea[0], titulo, desc, estado)
                    print("Tarea actualizada.\n")
                    return
            print("Tarea no encontrada.\n")
            return
    print("Usuario no encontrado.\n")


def eliminar_tarea(usuarios, id_usuario):
    for usuario in usuarios:
        if usuario[0] == id_usuario:
            if not usuario[4]:
                print("Este usuario no tiene tareas.\n")
                return
            id_tarea = input("ID de la tarea a eliminar: ")
            for i, tarea in enumerate(usuario[4]):
                if tarea[0] == id_tarea:
                    usuario[4].pop(i)
                    print("Tarea eliminada.\n")
                    return
            print("Tarea no encontrada.\n")
            return
    print("Usuario no encontrado.\n")


def menu_tareas(usuarios, id_usuario):
    while True:
        print("#### MENÚ TAREAS #####")
        print("1. Agregar Tarea")
        print("2. Ver Tareas")
        print("3. Total Tareas por Estado")
        print("4. Actualizar Tarea")
        print("5. Eliminar Tarea")
        print("6. Volver al Menú Principal")
        opcion = input("Elige una opción: ")
        print()

        match opcion:
            case "1":
                agregar_tarea(usuarios, id_usuario)
            case "2":
                ver_tareas(usuarios, id_usuario)
            case "3": 
                total_tareas_por_estado(usuarios)
            case "4":
                actualizar_tarea(usuarios, id_usuario)
            case "5":
                eliminar_tarea(usuarios, id_usuario)
            case "6":
                break
            case _:
                print("Opción inválida, elija una que esté en el menú.\n")


def menu_principal():
    usuarios = []
    while True:
        print("#### MENÚ PRINCIPAL ####")
        print("1. Agregar Usuario")
        print("2. Ver Usuarios")
        print("3. Actualizar Usuario")
        print("4. Eliminar Usuario")
        print("5. Gestionar Tareas")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        print()

        match opcion:
            case "1":
                agregar_usuario(usuarios)
            case "2":
                ver_usuarios(usuarios)
            case "3":
                actualizar_usuario(usuarios)
            case "4":
                eliminar_usuario(usuarios)
            case "5":
                id_usuario = input("ID del usuario: ")
                print()
                menu_tareas(usuarios, id_usuario)
            case "6":
                print("El programa cerró.")
                break
            case _:
                print("Opción inválida, elija una que esté en el menú.\n")

##################################################################
menu_principal()






