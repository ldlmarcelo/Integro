import os
import django
import random
from faker import Faker

# Configura Django para que funcione fuera del contexto del servidor web
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InventarioIT.settings')
django.setup()

from inventario.models import (
    Gerencia, CustomUser, TipoDispositivo, CantidadMemoria,
    Marca, TipoMemoria, Modelo, Estado, Ubicacion,
    Caracteristica, CaracteristicaEspecifica, Dispositivo,
    DispositivoCaracteristica, DispositivoEstado,
    DispositivoUbicacion, DispositivoPropietarioHistorico
)

def populate_db(num_registros=10):  # Puedes ajustar el número de registros a generar
    fake = Faker('es_ES')  # Para datos en español (puedes cambiar el locale si necesitas otro idioma)

    print(f"Poblando la base de datos con {num_registros} registros ficticios...")

    # --- Crear Gerencias ---
    gerencias = []
    print("Creando Gerencias...")
    for _ in range(3):  # Crear 3 gerencias de ejemplo
        nombre_gerencia = fake.company() + " Gerencia"  # Nombre de empresa ficticio + "Gerencia"
        gerencia, created = Gerencia.objects.get_or_create(nombre=nombre_gerencia)
        if created:
            print(f"  Gerencia creada: {gerencia}")
        else:
            print(f"  Gerencia ya existente: {gerencia}")
        gerencias.append(gerencia)

    # --- Crear Usuarios (CustomUser) ---
    print("Creando Usuarios...")
    for _ in range(num_registros):
        username = fake.user_name()
        email = fake.email()
        first_name = fake.first_name()
        last_name = fake.last_name()
        password = 'password123'  # Contraseña sencilla para todos los usuarios ficticios
        gerencia_usuario = random.choice(gerencias)  # Asignar gerencia aleatoria de las gerencias creadas

        user, created = CustomUser.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'password': password,
                'gerencia': gerencia_usuario
            }
        )
        if created:
            print(f"  Usuario creado: {user} (Gerencia: {gerencia_usuario})")
        else:
            print(f"  Usuario ya existente: {user}")

    # --- Crear Tipos de Dispositivo (Ejemplos) ---
    tipos_dispositivo = ["Notebook", "PC de Escritorio", "Monitor", "Impresora", "Router", "Switch"]
    tipos_dispositivo_objs = []
    print("Creando Tipos de Dispositivo...")
    for tipo_nombre in tipos_dispositivo:
        tipo_dispositivo, created = TipoDispositivo.objects.get_or_create(nombre=tipo_nombre)
        if created:
            print(f"  Tipo de Dispositivo creado: {tipo_dispositivo}")
        else:
            print(f"  Tipo de Dispositivo ya existente: {tipo_dispositivo}")
        tipos_dispositivo_objs.append(tipo_dispositivo)

    # --- Crear Cantidades de Memoria (Ejemplos) ---
    cantidades_memoria = ["4GB", "8GB", "16GB", "32GB", "64GB"]  # ¡OJO! Ahora CantidadMemoria.cantidad es IntegerField!
    cantidades_memoria_objs = []
    print("Creando Cantidades de Memoria...")
    for cantidad_memoria_str in cantidades_memoria:
        cantidad_memoria_int = int(cantidad_memoria_str.replace("GB", ""))  # Convertir "4GB" a 4 (int)
        cantidad_memoria, created = CantidadMemoria.objects.get_or_create(cantidad=cantidad_memoria_int)
        if created:
            print(f"  Cantidad de Memoria creada: {cantidad_memoria}")
        else:
            print(f"  Cantidad de Memoria ya existente: {cantidad_memoria}")
        cantidades_memoria_objs.append(cantidad_memoria)

    # --- Crear Marcas (Ejemplos) ---
    marcas = ["HP", "Dell", "Lenovo", "Samsung", "Apple", "Microsoft", "Cisco", "TP-Link"]
    marcas_objs = []
    print("Creando Marcas...")
    for marca_nombre in marcas:
        marca, created = Marca.objects.get_or_create(nombre=marca_nombre)
        if created:
            print(f"  Marca creada: {marca}")
        else:
            print(f"  Marca ya existente: {marca}")
        marcas_objs.append(marca)

    # --- Crear Tipos de Memoria (Ejemplos) ---
    tipos_memoria_nombres = ["DDR4", "DDR5", "SDRAM", "GDDR6"]
    tipos_memoria_objs = []
    print("Creando Tipos de Memoria...")
    for tipo_memoria_nombre in tipos_memoria_nombres:
        tipo_memoria, created = TipoMemoria.objects.get_or_create(nombre=tipo_memoria_nombre)
        if created:
            print(f"  Tipo de Memoria creado: {tipo_memoria}")
        else:
            print(f"  Tipo de Memoria ya existente: {tipo_memoria}")
        tipos_memoria_objs.append(tipo_memoria)

    # --- Crear Modelos (Relacionados con Marcas - Ejemplos) ---
    print("Creando Modelos...")
    for _ in range(10):  # Crear 10 modelos de ejemplo
        nombre_modelo = fake.word().capitalize() + " " + str(fake.random_number(digits=3))  # "Ejemplo 123"
        marca_modelo = random.choice(marcas_objs)  # Asignar marca aleatoria
        modelo, created = Modelo.objects.get_or_create(nombre=nombre_modelo, marca_id_marca=marca_modelo)
        if created:
            print(f"  Modelo creado: {modelo}")
        else:
            print(f"  Modelo ya existente: {modelo}")

    # --- Crear Estados (Ejemplos) ---
    estados = ["Activo", "Inactivo", "En Reparación", "Dado de Baja", "En Almacén"]
    estados_objs = []
    print("Creando Estados...")
    for estado_nombre in estados:
        estado, created = Estado.objects.get_or_create(nombre=estado_nombre)
        if created:
            print(f"  Estado creado: {estado}")
        else:
            print(f"  Estado ya existente: {estado}")
        estados_objs.append(estado)

    # --- Crear Ubicaciones (Ejemplos) ---
    print("Creando Ubicaciones...")
    for _ in range(5):  # Crear 5 ubicaciones de ejemplo
        agencia = fake.city() + " Agencia"
        piso = str(fake.random_int(min=1, max=10))  # Piso ficticio
        ubicacion, created = Ubicacion.objects.get_or_create(agencia=agencia, piso=piso)
        if created:
            print(f"  Ubicación creada: {ubicacion}")
        else:
            print(f"  Ubicación ya existente: {ubicacion}")

    # --- Crear Características Generales (Ejemplos) ---
    caracteristicas_generales = ["RAM", "Procesador", "Pantalla", "Teclado", "Mouse", "Tarjeta de Red", "Velocidad de Red", "Interfaz de Conexión", "Resolución", "Tamaño", "Tipo de Teclado", "Tipo de Mouse"]
    caracteristicas_generales_objs = []
    print("Creando Características Generales...")
    for caracteristica_nombre in caracteristicas_generales:
        caracteristica, created = Caracteristica.objects.get_or_create(nombre=caracteristica_nombre)
        if created:
            print(f"  Característica General creada: {caracteristica}")
        else:
            print(f"  Característica General ya existente: {caracteristica}")
        caracteristicas_generales_objs.append(caracteristica)

    # --- Crear Características Específicas (Ejemplos - Limitado por ahora) ---
    print("Creando Características Específicas (Limitado por ahora)...")
    tipos_dispositivo_ejemplo = [tipos_dispositivo_objs[0], tipos_dispositivo_objs[1], tipos_dispositivo_objs[2]]  # Notebook, PC, Monitor
    caracteristicas_ejemplo = [caracteristicas_generales_objs[0], caracteristicas_generales_objs[1], caracteristicas_generales_objs[2], caracteristicas_generales_objs[3], caracteristicas_generales_objs[4], caracteristicas_generales_objs[5], caracteristicas_generales_objs[6]]  # RAM, Procesador, Pantalla, Teclado, Mouse, Tarjeta de Red, Velocidad Red

    for _ in range(15):  # Crear 15 características específicas de ejemplo
        caracteristica_general = random.choice(caracteristicas_generales_objs)
        tipo_dispositivo_especifico = random.choice(tipos_dispositivo_ejemplo)

        # Simulación de datos específicos (puedes refinar esto)
        tipo_memoria_especifica = random.choice(tipos_memoria_objs) if caracteristica_general.nombre == "RAM" else None
        cantidad_memoria_especifica = random.choice(cantidades_memoria_objs) if caracteristica_general.nombre == "RAM" else None
        tipo_procesador_especifico = fake.word().capitalize() if caracteristica_general.nombre == "Procesador" else None
        velocidad_red_especifica = f"{fake.random_int(min=100, max=1000)} Mbps" if caracteristica_general.nombre == "Velocidad de Red" else None
        interfaz_conexion_especifica = random.choice(["Ethernet", "Wi-Fi", "Fibra"]) if caracteristica_general.nombre == "Interfaz de Conexión" else None

        caracteristica_especifica, created = CaracteristicaEspecifica.objects.get_or_create(
            caracteristica=caracteristica_general,
            tipo_dispositivo=tipo_dispositivo_especifico,
            defaults={
                'tipo_memoria': tipo_memoria_especifica,
                'cantidad_memoria': cantidad_memoria_especifica,
                'tipo_procesador': tipo_procesador_especifico,
                'velocidad_red': velocidad_red_especifica,
                'interfaz_conexion': interfaz_conexion_especifica,
            }
        )
        if created:
            print(f"  Característica Específica creada: {caracteristica_especifica}")
        else:
            print(f"  Característica Específica ya existente: {caracteristica_especifica}")

    # --- Crear Dispositivos ---
    print("Creando Dispositivos...")
    for _ in range(num_registros):
        nomenclatura = fake.bothify(text='IT-????-###')  # Ej: IT-ABCD-123
        serie = fake.bothify(text='SN-##########')  # Ej: SN-ABCDEFGHIJ
        jira = fake.bothify(text='JIRA-#####')  # Ej: JIRA-12345
        tipo_dispositivo_dispositivo = random.choice(tipos_dispositivo_objs)
        propietario_dispositivo = random.choice(CustomUser.objects.all())  # Propietario aleatorio de los usuarios creados

        dispositivo, created = Dispositivo.objects.get_or_create(
            nomenclatura=nomenclatura,
            serie=serie,
            jira=jira,
            tipo_dispositivo=tipo_dispositivo_dispositivo,
            propietario=propietario_dispositivo,
        )
        if created:
            print(f"  Dispositivo creado: {dispositivo}")
        else:
            print(f"  Dispositivo ya existente: {dispositivo}")

        # --- Crear DispositivoCaracteristica para cada Dispositivo (Ejemplo - Limitado) ---
        num_caracteristicas_dispositivo = random.randint(1, 5)  # Aleatorio entre 1 y 5 caracteristicas por dispositivo

        # Obtener todas las características específicas para el tipo de dispositivo
        caracteristicas_disponibles = list(CaracteristicaEspecifica.objects.filter(tipo_dispositivo=tipo_dispositivo_dispositivo))

        # Asegurarse de que num_caracteristicas_dispositivo no sea mayor que el número de características disponibles
        num_caracteristicas_dispositivo = min(num_caracteristicas_dispositivo, len(caracteristicas_disponibles))

        # Seleccionar características aleatorias
        caracteristicas_especificas_dispositivo = random.sample(caracteristicas_disponibles, num_caracteristicas_dispositivo)

        for caracteristica_especifica in caracteristicas_especificas_dispositivo:
            valor_caracteristica = fake.word()  # Valor ficticio - DEBERÍAS REFINAR ESTO SEGÚN LA CARACTERÍSTICA
            dispositivo_caracteristica, created = DispositivoCaracteristica.objects.get_or_create(
                dispositivo_id_dispositivo=dispositivo,
                caracteristica_especifica=caracteristica_especifica,
                defaults={'valor': valor_caracteristica}
            )
            if created:
                print(f"    DispositivoCaracteristica creada: {dispositivo_caracteristica}")
            else:
                print(f"    DispositivoCaracteristica ya existente: {dispositivo_caracteristica}")

    print("Base de datos poblada con datos ficticios.")


if __name__ == '__main__':
    populate_db(num_registros=20)  # Ejecutar la función para poblar la base de datos al ejecutar el script