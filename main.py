from ListaEnlazada import ListaEnlazada
from datetime import datetime, date

# DATOS DEL PROGRAMA

comentarios = []
citas = []
ultimo_pedido = None


# COLORES 


rojo = "\033[91m"
verde = "\033[92m"
amarillo = "\033[93m"
azul = "\033[94m"
cian = "\033[96m"
naranja = "\033[38;5;208m"
blanco = "\033[97m"
reset = "\033[0m"

# MENÚS

entradas = {
    "Quesillo": 1.50,
    "Tostones": 2.00,
    "Cornetas": 1.75,
    "Ensalada de repollo": 1.25,
    "Papas": 1.50,
    "Chips de plátano": 1.75,
    "Chips de yuca": 1.75,
    "Chips de camote": 1.75,
    "Chips de zanahoria": 1.75
}

platos_fuertes = {
    "Pollo a la plancha": 5.00,
    "Pollo frito": 5.50,
    "Pollo al horno": 6.00,
    "Pollo a la barbacoa": 6.50
}

bebidas = {
    "Gaseosa": 0.50,
    "Jugo": 1.00
}

postres = {
    "Pastel": 1.50,
    "Helado": 1.00
}

# REALIZAR COMPRA

def realizar_compra(compras):
    categorias = {
        "1": ("Entradas", entradas),
        "2": ("Platos fuertes", platos_fuertes),
        "3": ("Bebidas", bebidas),
        "4": ("Postres", postres)
    }

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
                return True
            elif confirmar == "no":
                print(f"\n{amarillo}Puedes seguir modificando tu pedido.{reset}")
                continue
            else:
                print(f"\n{rojo}Respuesta inválida. Escribe sí o no.{reset}")
                continue

        if opcion == "6":
            print(f"\n{rojo}Has cancelado el pedido.{reset}")
            return False

        if opcion not in categorias:
            print(f"{rojo}Opción inválida.{reset}")
            continue

        nombre_categoria, productos = categorias[opcion]
        print(f"\n{amarillo}--- {nombre_categoria.upper()} ---{reset}")

        lista_productos = list(productos.items())
        for i, (nombre, precio) in enumerate(lista_productos, start=1):
            print(f"{i}. {nombre} - ${precio:.2f}")

        try:
            seleccion = int(input("Seleccione un producto: ").strip())
            if seleccion < 1 or seleccion > len(lista_productos):
                print(f"{rojo}Producto no válido.{reset}")
                continue

            nombre, precio = lista_productos[seleccion - 1]
            cantidad = int(input("Ingrese la cantidad: ").strip())

            if cantidad <= 0:
                print(f"{rojo}La cantidad debe ser mayor que cero.{reset}")
                continue
            if cantidad > 100:
                print(f"{rojo}La cantidad máxima por selección es 100.{reset}")
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

# AGENDAR CITA

def agendar_cita():
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

    for cita in citas:
        if cita["fecha"] == fecha_cita and cita["hora"] == hora_cita:
            print(f"{rojo}Ya existe una cita para esa fecha y hora.{reset}")
            return

    cita = {"nombre": nombre, "fecha": fecha_cita, "hora": hora_cita}
    citas.append(cita)

    print(f"\n{verde}¡Cita registrada correctamente!{reset}")
    print(f"Cliente: {nombre}")
    print(f"Fecha: {fecha_cita.strftime('%d/%m/%Y')}")
    print(f"Hora: {hora_cita.strftime('%H:%M')}")

# CONSULTAR CITAS

def ver_citas():
    print(f"\n{cian}========== CITAS AGENDADAS =========={reset}")

    if not citas:
        print(f"{amarillo}Todavía no hay citas registradas.{reset}")
        return

    for i, cita in enumerate(citas, start=1):
        print(f"\n{verde}Cita #{i}{reset}")
        print(f"Cliente: {cita['nombre']}")
        print(f"Fecha: {cita['fecha'].strftime('%d/%m/%Y')}")
        print(f"Hora: {cita['hora'].strftime('%H:%M')}")

# VER Y AGREGAR COMENTARIOS


comentarios = []
estrellas = []


def dar_comentario_y_estrellas():

    nombre = input("Ingrese su nombre: ")
    comentario = input("Escriba su comentario: ")

    while True:
        try:
            cantidad_estrellas = int(
                input("Califique el restaurante de 1 a 5 estrellas: ")
            )

            if 1 <= cantidad_estrellas <= 5:
                break
            else:
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


def ver_comentarios():

       if len(comentarios) > 0:

          print("\n===== COMENTARIOS DEL RESTAURANTE =====")

          for opinion in comentarios:
             print("Cliente:", opinion["nombre"])
             print("Comentario:", opinion["comentario"])
             print("Estrellas:", opinion["estrellas"], "/ 5")
             print("-----------------------------------")

       else:
           print("Todavía no hay comentarios.")


def ver_promedio_estrellas():

       if len(estrellas) > 0:

          calificacion = sum(estrellas) / len(estrellas)

          print(
            "Promedio del restaurante:",
            round(calificacion, 2),
            "estrellas"
        )

          print("Total de calificaciones:", len(estrellas))

       else:
          print("Todavía no hay calificaciones.")


def menu_opiniones():

       while True:

          print("\n===== OPINIONES DE SABOR NICARAGÜENSE =====")
          print("1. Dejar un comentario y calificar")
          print("2. Ver comentarios")
          print("3. Ver promedio de estrellas")
          print("4. Ver todas las calificaciones")
          print("5. Regresar al menú principal")

          opcion = input("Seleccione una opción: ")

          if opcion == "1":
            dar_comentario_y_estrellas()

          elif opcion == "2":
            ver_comentarios()

          elif opcion == "3":
            ver_promedio_estrellas()

          elif opcion == "4":
            print("Calificaciones recibidas:", estrellas)

          elif opcion == "5":
            break

          else:
            print("Seleccione una opción válida.")



# PEDIDO A DOMICILIO

def pedido_en_linea():
    global ultimo_pedido

    print(f"\n{cian}========== PEDIDO A DOMICILIO =========={reset}")
    respuesta = input(
        "¿Desea realizar un pedido a domicilio? (sí/no): "
    ).strip().casefold()

    if respuesta == "sí" or respuesta == "si":
        destino = input("Ingrese su ciudad o destino: ").strip()

        if not destino:
            print(f"{rojo}Debe ingresar un destino.{reset}")
            return

        destino_normalizado = destino.casefold()
        costo_envio = 0.00 if destino_normalizado in ("león", "leon") else 5.00

        compras = ListaEnlazada()
        pedido_valido = realizar_compra(compras)

        if not pedido_valido:
            print(f"{amarillo}No se procesará ningún cobro.{reset}")
            return

        subtotal = compras.calcular_total()
        total = subtotal + costo_envio

        ultimo_pedido = {
            "compras": compras,
            "destino": destino,
            "subtotal": subtotal,
            "envio": costo_envio,
            "total": total
        }

        print(f"\n{amarillo}========== TOTAL DEL PEDIDO =========={reset}")
        print(f"Destino: {destino}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Costo de envío: ${costo_envio:.2f}")
        print(f"{verde}Total con envío: ${total:.2f}{reset}")

    elif respuesta == "no":
        compras = ListaEnlazada()
        pedido_valido = realizar_compra(compras)

        if not pedido_valido:
            print(f"{amarillo}Pedido cancelado. No se realizará ningún cobro.{reset}")
            return

        total = compras.calcular_total()
        ultimo_pedido = {
            "compras": compras,
            "destino": "Sin domicilio",
            "subtotal": total,
            "envio": 0.00,
            "total": total
        }
        print(f"\n{verde}Total del pedido: ${total:.2f}{reset}")

    else:
        print(f"{rojo}Respuesta inválida. Escriba sí o no.{reset}")

# VER ÚLTIMA LISTA DE COMPRAS

def ver_lista_compras():
    print(f"\n{cian}========== LISTA DE COMPRAS =========={reset}")

    if ultimo_pedido is None:
        print(f"{amarillo}Todavía no hay pedidos confirmados en esta sesión.{reset}")
        return

    ultimo_pedido["compras"].mostrar()
    print(f"Destino: {ultimo_pedido['destino']}")
    print(f"Subtotal: ${ultimo_pedido['subtotal']:.2f}")
    print(f"Envío: ${ultimo_pedido['envio']:.2f}")
    print(f"{verde}Total: ${ultimo_pedido['total']:.2f}{reset}")

# MENÚ PRINCIPAL

def menu_principal():
    while True:
        print(f"\n{naranja}===================================={reset}")
        print(f"{cian}       RESTAURANTE SABOR NICA{reset}")
        print(f"{naranja}===================================={reset}")
        print("1. Ver menús y realizar pedidos")
        print("2. Agendar cita")
        print("3. ver comentario y calificar")
        print("4. Ver lista de compras")
        print("5. Ver citas agendadas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            pedido_en_linea()
        elif opcion == "2":
            agendar_cita()
        elif opcion == "3":
           dar_comentario_y_estrellas ()
        elif opcion == "4":
            ver_lista_compras()
        elif opcion == "5":
            ver_citas()
        elif opcion == "6":
            print(f"\n{verde}Gracias por visitar Sabor Nica.{reset}")
            break
        else:
            print(f"{rojo}Opción inválida. Intente nuevamente.{reset}")


if __name__ == "__main__":
    menu_principal()
