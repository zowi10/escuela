import sqlite3

conn = sqlite3.connect('escuela.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    grado TEXT NOT NULL,
    edad INTEGER NOT NULL,
    promedio REAL NOT NULL
)
''')
conn.commit()

def agregar_estudiante():
    nombre = input("Nombre del estudiante: ")
    grado = input("Grado (ej. 3ro A): ")
    edad = int(input("Edad: "))
    promedio = float(input("Promedio final: "))
    cursor.execute("INSERT INTO estudiantes (nombre, grado, edad, promedio) VALUES (?, ?, ?, ?)",
                   (nombre, grado, edad, promedio))
    conn.commit()
    print("✅ Estudiante agregado correctamente.")

def modificar_estudiante():
    id_estudiante = input("ID del estudiante a modificar: ")
    nombre = input("Nuevo nombre: ")
    grado = input("Nuevo grado: ")
    edad = int(input("Nueva edad: "))
    promedio = float(input("Nuevo promedio: "))
    cursor.execute("UPDATE estudiantes SET nombre = ?, grado = ?, edad = ?, promedio = ? WHERE id = ?",
                   (nombre, grado, edad, promedio, id_estudiante))
    conn.commit()
    print("✏️ Estudiante modificado exitosamente.")

def mostrar_estudiantes():
    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()
    print("📋 Lista de estudiantes:")
    for est in estudiantes:
        print(est)

def eliminar_estudiante():
    id_estudiante = input("ID del estudiante a eliminar: ")
    cursor.execute("DELETE FROM estudiantes WHERE id = ?", (id_estudiante,))
    conn.commit()
    print("🗑️ Estudiante eliminado correctamente.")

def buscar_estudiante():
    nombre = input("Buscar por nombre: ")
    cursor.execute("SELECT * FROM estudiantes WHERE nombre LIKE ?", ('%' + nombre + '%',))
    resultados = cursor.fetchall()
    print("🔍 Resultados de búsqueda:")
    for est in resultados:
        print(est)

def menu():
    while True:
        print("\n=== Sistema Escolar ===")
        print("1. Agregar estudiante")
        print("2. Modificar estudiante")
        print("3. Mostrar todos los estudiantes")
        print("4. Eliminar estudiante")
        print("5. Buscar estudiante")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ")

        match opcion:
            case "1":
                agregar_estudiante()
            case "2":
                modificar_estudiante()
            case "3":
                mostrar_estudiantes()
            case "4":
                eliminar_estudiante()
            case "5":
                buscar_estudiante()
            case "6":
                print("👋 Saliendo del sistema.")
                break
            case _:
                print("⚠️ Opción inválida, intenta nuevamente.")

if __name__ == "__main__":
    menu()
    conn.close()
