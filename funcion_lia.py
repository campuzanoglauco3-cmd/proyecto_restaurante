import json
import random
import time

Ruta = r"C:\Users\zayva\OneDrive\Desktop\proyect_sabor_nica\comidas.json"
# Colores ANSI para la consola
VERDE = "\033[92m"
CIAN = "\033[96m"
AMARILLO = "\033[93m"
ROJO = "\033[91m"
RESET = "\033[0m"

def decir_lia(texto, color=VERDE, velocidad=0.03):
    """Efecto mecanografiado letra por letra usando la librería time."""
    print(color, end="", flush=True)
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidad)
    print(RESET)

def cargar_comidas():
    """Carga los datos desde el archivo JSON de forma segura."""
    try:
        with open(Ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
            if not contenido:
                decir_lia(f"Error: El archivo en '{Ruta}' está vacío.", ROJO)
                return None
            return json.loads(contenido)
    except FileNotFoundError:
        decir_lia(f"Error: No se encontró el archivo en {Ruta}", ROJO)
        return None
    except json.JSONDecodeError:
        decir_lia("Error: El archivo JSON tiene un formato inválido o está corrupto.", ROJO)
        return None

comidas = cargar_comidas()

def buscar_por_presupuesto(presupuesto_max):
    if not comidas:
        return

    decir_lia(f"\n--- Opciones individuales por menos de ${presupuesto_max:.2f} ---", CIAN)
    encontrado = False

    for categoria, items in comidas.items():
        opciones_categoria = []
        for nombre, precio in items.items():
            if precio <= presupuesto_max:
                opciones_categoria.append((nombre, precio))
        
        if opciones_categoria:
            encontrado = True
            nombre_cat = categoria.replace('_', ' ').capitalize()
            decir_lia(f"\n📌 {nombre_cat}:", VERDE)
            for nombre, precio in opciones_categoria:
                print(f"  • {nombre}: ${precio:.2f}")

    if not encontrado:
        decir_lia("\nLo siento, no hay ningún producto individual en ese rango de precio.", ROJO)

def recomendar_combo_completo(presupuesto_max):
    """Genera una combinación de Plato Fuerte + Entrada + Bebida dentro del presupuesto."""
    if not comidas:
        return

    combos_posibles = []

    if not all(k in comidas for k in ["platos_fuertes", "entradas", "bebidas"]):
        decir_lia("El JSON no contiene las categorías requeridas ('platos_fuertes', 'entradas', 'bebidas').", ROJO)
        return

    for plato, p_precio in comidas["platos_fuertes"].items():
        for entrada, e_precio in comidas["entradas"].items():
            for bebida, b_precio in comidas["bebidas"].items():
                total = p_precio + e_precio + b_precio
                if total <= presupuesto_max:
                    combos_posibles.append({
                        "plato": plato,
                        "entrada": entrada,
                        "bebida": bebida,
                        "total": total
                    })

    if combos_posibles:
        combo = random.choice(combos_posibles)
        decir_lia(f"\n💡 ¡Te armé este Combo Completo por ${combo['total']:.2f}!", VERDE)
        print(f"  • Plato: {combo['plato']}")
        print(f"  • Entrada: {combo['entrada']}")
        print(f"  • Bebida: {combo['bebida']}")
    else:
        decir_lia(f"\nCon ${presupuesto_max:.2f} no nos alcanza para un combo completo (Plato + Entrada + Bebida).", AMARILLO)

def iniciar_asistente():
    """Lógica del menú interactivo de LIA con animación de texto."""
    if not comidas:
        return

    decir_lia("HOLA SOY LIA Y HOY SERÉ TU GUÍA GASTRONÓMICA 🤖🍔", VERDE, velocidad=0.04)
    
    while True:
        decir_lia("\n=== MENÚ DE CONSULTAS ===", CIAN, velocidad=0.01)
        print("1. Consultar opciones individuales por presupuesto")
        print("2. Recomendar un combo completo (Plato + Entrada + Bebida)")
        print("3. Salir")
        
        opcion = input(AMARILLO + "\nSelecciona una opción (1-3): " + RESET)
        
        if opcion in ["1", "2"]:
            try:
                monto = float(input(AMARILLO + "Ingresa tu presupuesto disponible ($): " + RESET))
                if opcion == "1":
                    buscar_por_presupuesto(monto)
                elif opcion == "2":
                    recomendar_combo_completo(monto)
            except ValueError:
                decir_lia("Por favor ingresa un monto numérico válido.", ROJO)
        elif opcion == "3":
            decir_lia("¡Hasta pronto! LIA se despide 👋", VERDE, velocidad=0.04)
            break
        else:
            decir_lia("Opción inválida, intenta nuevamente.", ROJO)

if __name__ == "__main__":
    iniciar_asistente()