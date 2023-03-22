class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)
<<<<<<< HEAD

    def listarTareas(self):
        for tarea in self.tareas:
            if tarea.estaLista():
                print(f"La tarea {tarea.obtenerNombre()} está lista")
        else: <<<<<<< Elimina esta
               print(f"La tarea {tarea.obtenerNombre()} no está lista")
=======
>>>>>>> 7c478b81751948d248dc358b5e9729504578c23f
