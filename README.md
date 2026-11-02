# PROYECTO SABOR NICA
## Organización y control de versiones

### 1. Descripción del proyecto
Sabor Nica es un proyecto de restaurante desarrollado en Python. El trabajo realizado en esta etapa consiste en organizar el código fuente en diferentes archivos según sus funcionalidades y utilizar Git y GitHub para controlar las versiones y conservar copias de seguridad.

### 2. Estructura del proyecto

```text
Proyecto_Restaurante/
│
├── main.py
├── ListaEnlazada.py
│
├── originales/
│   ├── main.py
│   └── ListaEnlazada.py
│
└── modulos/
    ├── colores.py
    ├── menus_proyecto.py
    ├── citas.py
    ├── opiniones.py
    ├── compras.py
    ├── pedidos.py
    └── menu_principal.py
```

### 3. Descripción de los archivos

| Archivo | Función |
|---|---|
| main.py | Programa principal original. |
| ListaEnlazada.py | Implementa una lista enlazada para almacenar productos. |
| colores.py | Contiene los colores utilizados en consola. |
| menus_proyecto.py | Contiene los productos y sus precios. |
| citas.py | Gestiona las citas del restaurante. |
| opiniones.py | Gestiona comentarios y calificaciones. |
| compras.py | Gestiona el proceso de compra. |
| pedidos.py | Gestiona los pedidos a domicilio y las listas de compras. |
| menu_principal.py | Contiene el menú principal de navegación. |

### 4. Control de versiones

Se utilizó Git para registrar los cambios del proyecto y GitHub para almacenar el repositorio de manera remota.

Se trabajó con dos ramas:

- **main:** conserva la versión original V1.0.
- **organizacion-proyecto:** contiene el trabajo de organización de los módulos.

### 5. Copias de seguridad

Se creó la carpeta `originales/` para conservar copias de `main.py` y `ListaEnlazada.py`, evitando perder los archivos originales.

### 6. Commits realizados

1. `V1.0 - Version inicial del proyecto`
2. `Respaldo de archivos originales`
3. `Organizacion inicial de modulos del proyecto`

### 7. Estado del trabajo

Se completó la organización inicial de los archivos, el respaldo de los originales y el almacenamiento del proyecto en GitHub.

La integración y las pruebas de funcionamiento conjunto de los módulos quedan pendientes.