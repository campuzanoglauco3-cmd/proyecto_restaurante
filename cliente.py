from datetime import datetime, date
from ListaEnlazada import ListaEnlazada
from funcion_lia import iniciar_asistente

# COLORES
rojo = "\033[91m"
verde = "\033[92m"
amarillo = "\033[93m"
azul = "\033[94m"
cian = "\033[96m"
reset = "\033[0m"
rojo_oscuro= "#C0392B"

# Datos que se conservan mientras el programa siga ejecutándose
citas = []
comentarios = []
estrellas = []
ultimo_pedido = None

#proseso de compra

def realizar_compra(entradas, platos_fuertes, bebidas, postres):
    """Permite seleccionar productos y confirma o cancela una compra."""
    categorias = {
        "1": ("Entradas", entradas),
        "2": ("Platos fuertes", platos_fuertes),
        "3": ("Bebidas", bebidas),
        "4": ("Postres", postres)
    }

    compras = ListaEnlazada()

    while True:
        print(f"\n{cian}========== SABOR NICA =========={reset}")
        print("1. Entradas")
        print("2. Platos fuertes")
        print("3. Bebidas")
        print("4. Postres")
        print("5. Finalizar y confirmar pedido")
        print("6. Cancelar pedido")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "5":
            if compras.esta_vacia():
                print(f"\n{rojo}No puedes finalizar un pedido vacío.{reset}")
                continue

            total = compras.calcular_total()
            print(f"\n{amarillo}========== RESUMEN DEL PEDIDO =========={reset}")
            compras.mostrar()
            print(f"\nTotal de productos: ${total:.2f}")
            confirmar = input("¿Deseas confirmar la compra? (si/no): ").strip().casefold()

            if confirmar in ("si", "sí"):
                print(f"\n{verde}¡Pedido confirmado correctamente!{reset}")
                return compras
            elif confirmar == "no":
                print(f"{amarillo}Puedes seguir modificando tu pedido.{reset}")
            else:
                print(f"{rojo}Respuesta inválida. Escribe sí o no.{reset}")
            continue

        if opcion == "6":
            print(f"\n{rojo}Has cancelado el pedido.{reset}")
            return None

        if opcion not in categorias:
            print(f"{rojo}Opción inválida.{reset}")
            continue

        nombre_categoria, productos = categorias[opcion]
        print(f"\n{amarillo}--- {nombre_categoria.upper()} ---{reset}")
        lista_productos = list(productos.items())

        if not lista_productos:
            print("No hay productos registrados en esta categoría.")
            continue

        for indice, (nombre, precio) in enumerate(lista_productos, start=1):
            print(f"{indice}. {nombre} - ${precio:.2f}")

        try:
            seleccion = int(input("Seleccione un producto: ").strip())
            if seleccion < 1 or seleccion > len(lista_productos):
                print(f"{rojo}Producto no válido.{reset}")
                continue

            nombre, precio = lista_productos[seleccion - 1]
            cantidad = int(input("Ingrese la cantidad: ").strip())

            if cantidad <= 0 or cantidad > 100:
                print(f"{rojo}La cantidad debe estar entre 1 y 100.{reset}")
                continue

            compras.agregar(nombre, precio, cantidad)
            subtotal = precio * cantidad
            print(f"\n{verde}¡Producto agregado correctamente!{reset}")
            print(f"Producto: {nombre}")
            print(f"Cantidad: {cantidad}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"{azul}Total acumulado: ${compras.calcular_total():.2f}{reset}")

        except ValueError:
            print(f"{rojo}Debe ingresar un número entero válido.{reset}")


def agendar_cita(citas):
    print(f"\n{cian}========== AGENDAR CITA =========={reset}")
    nombre = input("Nombre del cliente: ").strip()
    fecha_texto = input("Fecha (DD/MM/AAAA): ").strip()
    hora_texto = input("Hora (HH:MM, formato 24 horas): ").strip()

    if not nombre or not fecha_texto or not hora_texto:
        print(f"{rojo}Todos los campos son obligatorios.{reset}")
        return

    try:
        fecha_cita = datetime.strptime(fecha_texto, "%d/%m/%Y").date()
        hora_cita = datetime.strptime(hora_texto, "%H:%M").time()
    except ValueError:
        print(f"{rojo}Fecha u hora inválida. Utilice DD/MM/AAAA y HH:MM.{reset}")
        return

    if fecha_cita < date.today():
        print(f"{rojo}No puede agendar una fecha pasada.{reset}")
        return

    if fecha_cita == date.today() and hora_cita <= datetime.now().time():
        print(f"{rojo}No puede agendar una hora que ya pasó.{reset}")
        return

    for cita in citas:
        if cita["fecha"] == fecha_cita and cita["hora"] == hora_cita:
            print(f"{rojo}Ya existe una cita para esa fecha y hora.{reset}")
            return

    citas.append({"nombre": nombre, "fecha": fecha_cita, "hora": hora_cita})
    print(f"\n{verde}¡Cita registrada correctamente!{reset}")
    print(f"Cliente: {nombre}")
    print(f"Fecha: {fecha_cita.strftime('%d/%m/%Y')}")
    print(f"Hora: {hora_cita.strftime('%H:%M')}")

# ver quienes agendaron cita

def ver_citas(citas):
    print(f"\n{cian}========== CITAS AGENDADAS =========={reset}")
    if not citas:
        print(f"{amarillo}Todavía no hay citas registradas.{reset}")
        return

    for indice, cita in enumerate(citas, start=1):
        print(f"\n{verde}Cita #{indice}{reset}")
        print(f"Cliente: {cita['nombre']}")
        print(f"Fecha: {cita['fecha'].strftime('%d/%m/%Y')}")
        print(f"Hora: {cita['hora'].strftime('%H:%M')}")

# para dar tu opinion y calificarnos

def dar_comentario_y_estrellas(comentarios, estrellas):
    nombre = input("Ingrese su nombre: ").strip()
    comentario = input("Escriba su comentario: ").strip()

    if not nombre or not comentario:
        print(f"{rojo}El nombre y el comentario son obligatorios.{reset}")
        return

    while True:
        try:
            cantidad_estrellas = int(input("Califique el restaurante de 1 a 5 estrellas: "))
            if 1 <= cantidad_estrellas <= 5:
                break
            print("La calificación debe estar entre 1 y 5.")
        except ValueError:
            print("Ingrese un número entero válido.")

    comentarios.append({
        "nombre": nombre,
        "comentario": comentario,
        "estrellas": cantidad_estrellas
    })
    estrellas.append(cantidad_estrellas)
    print("\n¡Gracias por compartir su opinión!")
    print("Su comentario y calificación se guardaron correctamente.")


def ver_comentarios(comentarios):
    if not comentarios:
        print("Todavía no hay comentarios.")
        return

    print("\n===== COMENTARIOS DEL RESTAURANTE =====")
    for opinion in comentarios:
        print("Cliente:", opinion["nombre"])
        print("Comentario:", opinion["comentario"])
        print("Estrellas:", opinion["estrellas"], "/ 5")
        print("-----------------------------------")


def ver_promedio_estrellas(estrellas):
    if not estrellas:
        print("Todavía no hay calificaciones.")
        return

    calificacion = sum(estrellas) / len(estrellas)
    print("Promedio del restaurante:", round(calificacion, 2), "estrellas")
    print("Total de calificaciones:", len(estrellas))


def menu_opiniones(comentarios, estrellas):
    while True:
        print("\n===== OPINIONES DE SABOR NICARAGÜENSE =====")
        print("1. Dejar un comentario y calificar")
        print("2. Ver comentarios")
        print("3. Ver promedio de estrellas")
        print("4. Ver todas las calificaciones")
        print("5. Regresar al menú de atención al cliente")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            dar_comentario_y_estrellas(comentarios, estrellas)
        elif opcion == "2":
            ver_comentarios(comentarios)
        elif opcion == "3":
            ver_promedio_estrellas(estrellas)
        elif opcion == "4":
            print("Calificaciones recibidas:", estrellas)
        elif opcion == "5":
            break
        else:
            print("Seleccione una opción válida.")


def registrar_venta(compras, ventas):
    """Copia los productos de una compra confirmada al registro de ventas."""
    actual = compras.cabeza
    while actual is not None:
        ventas.append({
            "producto": actual.producto,
            "precio": actual.precio,
            "cantidad": actual.cantidad
        })
        actual = actual.sig


def pedido_en_linea(entradas, platos_fuertes, bebidas, postres, ventas):
    print(f"\n{cian}========== PEDIDO A DOMICILIO =========={reset}")
    respuesta = input("¿Desea realizar un pedido a domicilio? (sí/no): ").strip().casefold()

    if respuesta in ("sí", "si"):
        destino = input("Ingrese su ciudad o destino: ").strip()
        if not destino:
            print(f"{rojo}Debe ingresar un destino.{reset}")
            return None
        costo_envio = 0.00 if destino.casefold() in ("león", "leon") else 5.00
    elif respuesta == "no":
        destino = "Sin domicilio"
        costo_envio = 0.00
    else:
        print(f"{rojo}Respuesta inválida. Escriba sí o no.{reset}")
        return None

    compras = realizar_compra(entradas, platos_fuertes, bebidas, postres)
    if compras is None:
        print(f"{amarillo}Pedido cancelado. No se realizará ningún cobro.{reset}")
        return None

    subtotal = compras.calcular_total()
    total = subtotal + costo_envio
    registrar_venta(compras, ventas)

    print(f"\n{amarillo}========== TOTAL DEL PEDIDO =========={reset}")
    print(f"Destino: {destino}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Costo de envío: ${costo_envio:.2f}")
    print(f"{verde}Total del pedido: ${total:.2f}{reset}")

    return {
        "compras": compras,
        "destino": destino,
        "subtotal": subtotal,
        "envio": costo_envio,
        "total": total
    }


def ver_lista_compras(ultimo_pedido):
    print(f"\n{cian}========== LISTA DE COMPRAS =========={reset}")
    if ultimo_pedido is None:
        print(f"{amarillo}Todavía no hay pedidos confirmados en esta sesión.{reset}")
        return

    ultimo_pedido["compras"].mostrar()
    print(f"Destino: {ultimo_pedido['destino']}")
    print(f"Subtotal: ${ultimo_pedido['subtotal']:.2f}")
    print(f"Envío: ${ultimo_pedido['envio']:.2f}")
    print(f"{verde}Total: ${ultimo_pedido['total']:.2f}{reset}")


def menu_cliente(entradas, platos_fuertes, bebidas, postres, ventas):
    """Menú de atención al cliente; conserva sus datos durante la sesión."""
    global ultimo_pedido

    while True:
        print(f"\n{cian}===== ATENCIÓN AL CLIENTE ====={reset}")
        print("1. Ver menús y realizar pedidos")
        print("2. Agendar cita")
        print("3. Ver comentarios y calificar")
        print("4. Ver lista de compras")
        print("5. Ver citas agendadas")
        print("6. Regresar al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            pedido = pedido_en_linea(entradas, platos_fuertes, bebidas, postres, ventas)
            if pedido is not None:
                ultimo_pedido = pedido
        elif opcion == "2":
            agendar_cita(citas)
        elif opcion == "3":
            menu_opiniones(comentarios, estrellas)
        elif opcion == "4":
            ver_lista_compras(ultimo_pedido)
        elif opcion == "5":
            ver_citas(citas)
        elif opcion == "6":
            break
        else:
            print(f"{rojo}Opción inválida. Intente nuevamente.{reset}")
