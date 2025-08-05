class Tarea:
    def _init_(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

class GestorTareas:
    def _init_(self):
        self.tareas = []

    def agregar(self, descripcion):
        self.tareas.append(Tarea(descripcion))

    def listar(self):
        for i, tarea in enumerate(self.tareas, start=1):
            estado = "✔" if tarea.completada else "✘"
            print(f"{i}. {tarea.descripcion} [{estado}]")

    def completar(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_completada()

gestor = GestorTareas()
gestor.agregar("Aprender Python")
gestor.agregar("Hacer el proyecto final")
gestor.listar()
gestor.completar(0)
gestor.listar()
