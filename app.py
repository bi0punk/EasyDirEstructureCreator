import os

def create_project_structure(project_type, project_name):
    base_dir = os.path.join(os.getcwd(), project_name)

    if project_type == "simple":
        directories = [
            os.path.join(base_dir, "src"),
            os.path.join(base_dir, "tests"),
            os.path.join(base_dir, "docs")
        ]
        files = [
            os.path.join(base_dir, "README.md"),
            os.path.join(base_dir, ".gitignore")
        ]

    elif project_type == "flask":
        directories = [
            os.path.join(base_dir, "app"),
            os.path.join(base_dir, "app", "templates"),
            os.path.join(base_dir, "app", "static"),
            os.path.join(base_dir, "app", "routes"),
            os.path.join(base_dir, "tests")
        ]
        files = [
            os.path.join(base_dir, "app", "__init__.py"),
            os.path.join(base_dir, "app", "routes", "__init__.py"),
            os.path.join(base_dir, "config.py"),
            os.path.join(base_dir, "run.py"),
            os.path.join(base_dir, "README.md"),
            os.path.join(base_dir, ".gitignore")
        ]

    elif project_type == "flask_api":
        directories = [
            os.path.join(base_dir, "app"),
            os.path.join(base_dir, "app", "models"),
            os.path.join(base_dir, "app", "resources"),
            os.path.join(base_dir, "app", "schemas"),
            os.path.join(base_dir, "tests")
        ]
        files = [
            os.path.join(base_dir, "app", "__init__.py"),
            os.path.join(base_dir, "app", "models", "__init__.py"),
            os.path.join(base_dir, "app", "resources", "__init__.py"),
            os.path.join(base_dir, "app", "schemas", "__init__.py"),
            os.path.join(base_dir, "config.py"),
            os.path.join(base_dir, "run.py"),
            os.path.join(base_dir, "README.md"),
            os.path.join(base_dir, ".gitignore")
        ]

    else:
        print("Tipo de proyecto no reconocido. Use 'simple', 'flask', o 'flask_api'.")
        return

    # Crear directorios
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Crear archivos vacíos
    for file in files:
        with open(file, 'w') as f:
            pass

    print(f"Estructura del proyecto '{project_name}' creada con éxito.")

if __name__ == "__main__":
    project_type = input("Ingrese el tipo de proyecto (simple, flask, flask_api): ")
    project_name = input("Ingrese el nombre del proyecto: ")
    create_project_structure(project_type, project_name)
