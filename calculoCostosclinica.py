# carlos_Alberto_ochoa
# 362
# 2

def validar(codigo):
    """
    Recibe un entero y retorna 1 si tiene 5 dígitos, 0 si no.
    """
    if 10000 <= codigo <= 99999:
        return 1
    else:
        return 0


def tipo(codigo):
    """
    Recibe el código (int) y retorna "AFILIADO" o "PARTICULAR"
    basado en el primer dígito.
    """
    # Usamos división entera para obtener el primer dígito
    primer_digito = codigo // 10000

    if primer_digito == 1:
        return "AFILIADO"
    elif primer_digito == 2:
        return "PARTICULAR"
    else:
        # Aunque 'validar' ya revisó esto, es buena práctica
        return "INVALIDO"


def servicio(codigo):
    """
    Recibe el código (int) y retorna el nombre del servicio
    basado en el segundo dígito.
    """
    # (codigo // 1000) nos da los primeros dos dígitos (ej: 12)
    # (% 10) nos da el último dígito de ese resultado (ej: 2)
    segundo_digito = (codigo // 1000) % 10

    if segundo_digito == 1:
        return "Radiografía"
    elif segundo_digito == 2:
        return "Ecografía"
    elif segundo_digito == 3:
        return "Laboratorio"
    elif segundo_digito == 4:
        return "Consulta Externa"
    elif segundo_digito == 5:
        return "Consulta Especializada"
    else:
        # Para cualquier otro dígito (0, 6, 7, 8, 9)
        return "OTRO"


def costo(nombre_servicio):
    """
    Recibe el nombre del servicio (string) y retorna
    su costo base (int).
    """
    if nombre_servicio == "Radiografía":
        return 30000
    elif nombre_servicio == "Ecografía":
        return 35000
    elif nombre_servicio == "Laboratorio":
        return 25000
    elif nombre_servicio == "Consulta Externa":
        return 40000
    elif nombre_servicio == "Consulta Especializada":
        return 80000
    elif nombre_servicio == "OTRO":
        return 0
    else:
        return 0


def descuReca(codigo, tipo_paciente, costo_base):
    """
    Recibe el código (int), tipo (string) y costo base (int).
    Calcula el valor del descuento (negativo) o recargo (positivo).
    """
    # Obtenemos los últimos 3 dígitos
    digito3 = (codigo // 100) % 10
    digito4 = (codigo // 10) % 10
    digito5 = codigo % 10

    suma_ultimos_tres = digito3 + digito4 + digito5

    tasa_modificacion = 0.0

    # Verificamos si la suma es par
    if suma_ultimos_tres % 2 == 0:
        # Suma PAR
        if tipo_paciente == "AFILIADO":
            tasa_modificacion = -0.15  # 15% Descuento
        else:  # PARTICULAR
            tasa_modificacion = 0.15  # 15% Recargo
    else:
        # Suma IMPAR
        if tipo_paciente == "AFILIADO":
            tasa_modificacion = -0.25  # 25% Descuento
        else:  # PARTICULAR
            tasa_modificacion = 0.25  # 25% Recargo

    # Retorna el valor monetario del descuento/recargo
    return costo_base * tasa_modificacion


def pago(costo_base, valor_descu_reca):
    """
    Recibe el costo base y el valor del descuento/recargo.
    Retorna el total a pagar.
    """
    # Simplemente suma, ya que el descuento ya viene negativo
    return costo_base + valor_descu_reca


def principal():
    """
    Función principal que orquesta el programa.
    """
    print("--- CÁLCULO DE COSTOS DE CLÍNICA ---")

    # 1. Captura del código
    codigo_str = input("Ingrese el código del paciente (5 dígitos): ")

    codigo_int = 0
    # Convertimos a entero, manejando si escribe letras
    try:
        codigo_int = int(codigo_str)
    except ValueError:
        print("Error: Debe ingresar solo números.")
        return  # Termina el programa si no es un número

    # 2. Verificación de validez
    if validar(codigo_int) == 1:
        # 3. Determinación de datos

        # Obtenemos los datos llamando a las funciones
        tipo_paciente = tipo(codigo_int)
        nombre_servicio = servicio(codigo_int)
        costo_base = costo(nombre_servicio)

        valor_descu_reca = descuReca(codigo_int, tipo_paciente, costo_base)

        total_a_pagar = pago(costo_base, valor_descu_reca)

        # 4. Mostrar resultados
        print("\n--- RESUMEN DEL PACIENTE ---")
        print(f"Código:         {codigo_int}")
        print(f"Tipo Paciente:  {tipo_paciente}")
        print(f"Servicio:       {nombre_servicio}")
        print("-------------------------------")
        print(f"Costo Base:       ${costo_base:,.0f}")

        # Mostramos si fue descuento o recargo
        if valor_descu_reca < 0:
            print(f"Descuento:        ${valor_descu_reca:,.0f}")
        else:
            print(f"Recargo:          ${valor_descu_reca:,.0f}")

        print(f"Total a Pagar:    ${total_a_pagar:,.0f}")

    else:
        # Si validar(codigo_int) retorna 0
        print("Error: El código ingresado no es válido.")
        print("Debe ser un número entero de exactamente 5 dígitos.")


# --- Ejecución del Programa ---
if __name__ == "__main__":
    principal()