# MÓDULO DE ADMINISTRACIÓN DE SABOR NICA

rojo = "\033[91m"
verde = "\033[92m"
amarillo = "\033[93m"
cian = "\033[96m"
reset = "\033[0m"


def agregar_platillo(categorias, costos_platillos):
    print("\n===== AGREGAR PLATILLO =====")
    print("1. Entradas")
    print("2. Platos fuertes")
    print("3. Bebidas")
    print("4. Postres")
    opcion = input("Seleccione la categoría: ").strip()

    if opcion not in categorias:
        print(f"{rojo}Categoría inválida.{reset}")
        return

    nombre_categoria, productos = categorias[opcion]
    nombre = input("Nombre del nuevo platillo: ").strip()
    if not nombre:
        print(f"{rojo}El nombre no puede estar vacío.{reset}")
        return
    if nombre in productos:
        print(f"{amarillo}Ese platillo ya existe en esta categoría.{reset}")
        return

    try:
        precio = float(input("Precio de venta ($): "))
        costo = float(input("Costo de preparación ($): "))
        if precio <= 0 or costo < 0:
            print(f"{rojo}El precio debe ser mayor que cero y el costo no puede ser negativo.{reset}")
            return
    except ValueError:
        print(f"{rojo}Ingrese valores numéricos válidos.{reset}")
        return

    productos[nombre] = precio
    costos_platillos[nombre] = costo
    print(f"{verde}{nombre} se agregó correctamente en {nombre_categoria}.{reset}")


def ver_platillos(categorias):
    print("\n===== PLATILLOS DISPONIBLES =====")
    for nombre_categoria, productos in categorias.values():
        print(f"\n--- {nombre_categoria.upper()} ---")
        if not productos:
            print("No hay productos registrados.")
        for nombre, precio in productos.items():
            print(f"{nombre}: ${precio:.2f}")


def configurar_costos(categorias, costos_platillos):
    todos = {}
    for _, productos in categorias.values():
        todos.update(productos)

    nombres = list(todos.keys())
    if not nombres:
        print("No hay platillos registrados.")
        return

    print("\n===== COSTOS DE PREPARACIÓN =====")
    for indice, nombre in enumerate(nombres, start=1):
        print(f"{indice}. {nombre} - Precio: ${todos[nombre]:.2f}")

    try:
        seleccion = int(input("Seleccione el producto: "))
        if seleccion < 1 or seleccion > len(nombres):
            print(f"{rojo}Selección inválida.{reset}")
            return
        nombre = nombres[seleccion - 1]
        costo = float(input(f"Costo de preparación de {nombre} ($): "))
        if costo < 0:
            print(f"{rojo}El costo no puede ser negativo.{reset}")
            return
        costos_platillos[nombre] = costo
        print(f"{verde}Costo actualizado correctamente.{reset}")
    except ValueError:
        print(f"{rojo}Ingrese valores numéricos válidos.{reset}")


def consultar_ganancias(ventas, costos_platillos):
    if not ventas:
        print(f"{amarillo}Todavía no hay ventas confirmadas en esta sesión.{reset}")
        return

    ingresos = 0
    costos = 0
    productos_sin_costo = set()

    for venta in ventas:
        ingresos += venta["precio"] * venta["cantidad"]
        nombre = venta["producto"]
        if nombre not in costos_platillos:
            productos_sin_costo.add(nombre)
        else:
            costos += costos_platillos[nombre] * venta["cantidad"]

    print("\n===== REPORTE ADMINISTRATIVO =====")
    print(f"Ingresos por ventas: ${ingresos:.2f}")
    print(f"Costos de preparación registrados: ${costos:.2f}")

    if productos_sin_costo:
        print(f"{amarillo}No se puede calcular la ganancia exacta.{reset}")
        print("Registre el costo de preparación de:")
        for nombre in sorted(productos_sin_costo):
            print(f"- {nombre}")
    else:
        ganancia = ingresos - costos
        print(f"{verde}Ganancia antes de otros gastos: ${ganancia:.2f}{reset}")


def menu_administrador(entradas, platos_fuertes, bebidas, postres, ventas, costos_platillos):
    clave = input("Ingrese la contraseña administrativa: ")
    if clave != "Sabor123":
        print(f"{rojo}Contraseña incorrecta.{reset}")
        return

    categorias = {
        "1": ("Entradas", entradas),
        "2": ("Platos fuertes", platos_fuertes),
        "3": ("Bebidas", bebidas),
        "4": ("Postres", postres)
    }

    print(f"{verde}Acceso autorizado.{reset}")
    while True:
        print(f"\n{cian}===== PANEL ADMINISTRATIVO ====={reset}")
        print("1. Agregar platillo")
        print("2. Ver platillos disponibles")
        print("3. Configurar costos de preparación")
        print("4. Consultar ganancias")
        print("5. Regresar al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_platillo(categorias, costos_platillos)
        elif opcion == "2":
            ver_platillos(categorias)
        elif opcion == "3":
            configurar_costos(categorias, costos_platillos)
        elif opcion == "4":
            consultar_ganancias(ventas, costos_platillos)
        elif opcion == "5":
            break
        else:
            print(f"{rojo}Opción inválida.{reset}")
