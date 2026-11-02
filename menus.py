from cliente import menu_cliente
from administracion import menu_administrador
from funcion_lia import iniciar_asistente

# MENÚS Y PRODUCTOS COMPARTIDOS POR CLIENTES Y ADMINISTRADORES
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

# INFORMACIÓN COMPARTIDA DURANTE LA EJECUCIÓN
ventas = []
costos_platillos = {}

# COLORES
rojo = "\033[91m"
verde = "\033[92m"
cian = "\033[96m"
naranja = "\033[38;5;208m"
reset = "\033[0m"


def menu_principal():
    while True:
        print(f"\n{naranja}===================================={reset}")
        print(f"{cian}       RESTAURANTE SABOR NICA{reset}")
        print(f"{naranja}===================================={reset}")
        print("1. Atención al cliente")
        print("2. Administración")
        print("3. Lia")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_cliente(entradas, platos_fuertes, bebidas, postres, ventas)
        elif opcion == "2":
            menu_administrador(
                entradas,
                platos_fuertes,
                bebidas,
                postres,
                ventas,
                costos_platillos
            )
        elif opcion == "3":
            iniciar_asistente()
        elif opcion == "4":
            print(f"{verde}¡Gracias por visitar Sabor Nica! ¡Hasta luego!{reset}")
            break
        else:
            print(f"{rojo}Opción inválida. Intente nuevamente.{reset}")
