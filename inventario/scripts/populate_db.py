import datetime
from django.contrib.auth.models import Group
from django.utils import timezone
from inventario.models import (
    Gerencia,
    TipoDispositivo,
    EstadoDispositivo,
    Ubicacion,
    Marca,
    Modelo,
    Caracteristica,
    CantidadMemoria,
    TipoMemoria,
    CustomUser,
    Dispositivo,
    CaracteristicaEspecifica,
    DispositivoCaracteristica,
    DispositivoEstado,
    DispositivoUbicacion,
    DispositivoPropietarioHistorico,
)


def run():
    print("Iniciando población de la base de datos...")

    # --- 1. Modelos de Catálogo ---
    print("Poblando modelos de catálogo...")

    # Gerencias
    gerencias = ["Informática", "Administración", "Recursos Humanos", "Ventas", "Finanzas", "Marketing"] # Añadí más gerencias para variedad
    gerencias_obj = {} # Diccionario para guardar objetos Gerencia y acceder por nombre
    for nombre_gerencia in gerencias:
        gerencia, created = Gerencia.objects.get_or_create(nombre=nombre_gerencia)
        gerencias_obj[nombre_gerencia] = gerencia # Guardar en el diccionario

    # Tipos de Dispositivo
    tipos_dispositivo = ["Notebook", "Monitor", "Teclado", "Mouse", "Smartphone", "Tablet", "Impresora", "Proyector", "Auriculares"] # Añadí más tipos
    tipos_dispositivo_obj = {} # Diccionario para guardar objetos TipoDispositivo
    for nombre_tipo in tipos_dispositivo:
        tipo_dispositivo, created = TipoDispositivo.objects.get_or_create(nombre=nombre_tipo)
        tipos_dispositivo_obj[nombre_tipo] = tipo_dispositivo # Guardar en el diccionario

    # Estados de Dispositivo
    estados_dispositivo = ["Disponible", "En uso", "En reparación", "Obsoleto", "Dado de baja", "Almacenado", "Prestado"] # Añadí más estados
    estados_dispositivo_obj = {} # Diccionario para guardar objetos EstadoDispositivo
    for nombre_estado in estados_dispositivo:
        estado_dispositivo, created = EstadoDispositivo.objects.get_or_create(nombre=nombre_estado)
        estados_dispositivo_obj[nombre_estado] = estado_dispositivo # Guardar en el diccionario

    # Ubicaciones
    ubicaciones = [
        {"agencia": "Casa Central", "piso": "1"},
        {"agencia": "Casa Central", "piso": "2"},
        {"agencia": "Sucursal Norte", "piso": "Planta Baja"},
        {"agencia": "Sucursal Sur", "piso": "Entrepiso"},
        {"agencia": "Depósito", "piso": "Único"}, # Nueva ubicación
    ]
    ubicaciones_obj = {} # Diccionario para guardar objetos Ubicacion
    for ubicacion_data in ubicaciones:
        ubicacion, created = Ubicacion.objects.get_or_create(**ubicacion_data)
        ubicaciones_obj[f"{ubicacion.agencia}-{ubicacion.piso}"] = ubicacion # Clave más descriptiva

    # Marcas
    marcas = ["Lenovo", "HP", "Dell", "Apple", "Samsung", "Logitech", "Microsoft", "Xiaomi", "Brother"] # Añadí más marcas
    marcas_obj = {} # Diccionario para guardar objetos Marca
    for nombre_marca in marcas:
        marca, created = Marca.objects.get_or_create(nombre=nombre_marca)
        marcas_obj[nombre_marca] = marca # Guardar en el diccionario

    # Cantidades de Memoria
    cantidades_memoria = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 27] # Añadí más cantidades (hasta 1TB = 1024GB)
    cantidades_memoria_obj = {} # Diccionario para guardar objetos CantidadMemoria
    for cantidad in cantidades_memoria:
        cantidad_memoria, created = CantidadMemoria.objects.get_or_create(cantidad=cantidad)
        cantidades_memoria_obj[cantidad] = cantidad_memoria # Guardar en el diccionario

    # Tipos de Memoria
    tipos_memoria = ["DDR3", "DDR4", "DDR5", "SDRAM", "GDDR6", "LPDDR5"] # Añadí más tipos de memoria
    tipos_memoria_obj = {} # Diccionario para guardar objetos TipoMemoria
    for nombre_tipo_memoria in tipos_memoria:
        tipo_memoria, created = TipoMemoria.objects.get_or_create(nombre=nombre_tipo_memoria)
        tipos_memoria_obj[nombre_tipo_memoria] = tipo_memoria # Guardar en el diccionario

    # Características Generales
    caracteristicas_generales = ["RAM", "Disco Duro", "Procesador", "Pantalla", "Teclado", "Mouse", "Sistema Operativo", "Office", "Antivirus", "Resolución", "Tamaño", "Velocidad", "Conectividad"] # Añadí más características
    caracteristicas_obj = {} # Diccionario para guardar objetos Caracteristica
    for nombre_caracteristica in caracteristicas_generales:
        caracteristica, created = Caracteristica.objects.get_or_create(nombre=nombre_caracteristica)
        caracteristicas_obj[nombre_caracteristica] = caracteristica # Guardar en el diccionario


    # --- 2. Características Específicas (Ejemplos más completos y variados) ---
    print("Poblando Características Específicas...")

    # Notebook - RAM DDR4 16GB
    CaracteristicaEspecifica.objects.get_or_create(
        caracteristica=caracteristicas_obj["RAM"],
        tipo_dispositivo=tipos_dispositivo_obj["Notebook"],
        tipo_memoria=tipos_memoria_obj["DDR4"],
        cantidad_memoria=cantidades_memoria_obj[16],
    )
    # Notebook - Disco Duro SSD 512GB
    CaracteristicaEspecifica.objects.get_or_create(
        caracteristica=caracteristicas_obj["Disco Duro"],
        tipo_dispositivo=tipos_dispositivo_obj["Notebook"],
        tipo_memoria=tipos_memoria_obj["SDRAM"], # SDRAM es genérico para SSD
        cantidad_memoria=cantidades_memoria_obj[512],
        tipo_procesador="SSD",
    )
    # Notebook - Procesador Intel Core i7
    CaracteristicaEspecifica.objects.get_or_create(
        caracteristica=caracteristicas_obj["Procesador"],
        tipo_dispositivo=tipos_dispositivo_obj["Notebook"],
        tipo_procesador="Intel Core i7",
    )
    # Monitor - Pantalla 27 pulgadas, Resolución 1920x1080, HDMI
    CaracteristicaEspecifica.objects.get_or_create(
        caracteristica=caracteristicas_obj["Pantalla"],
        tipo_dispositivo=tipos_dispositivo_obj["Monitor"],
        interfaz_conexion="HDMI",
        cantidad_memoria=cantidades_memoria_obj[27], # Usando cantidad_memoria para "tamaño" en pulgadas (reutilizando modelo)
        tipo_procesador="1920x1080", # Usando tipo_procesador para "resolución" (reutilizando modelo)
    )
    # Teclado - Conectividad USB, Característica "Teclado"
    CaracteristicaEspecifica.objects.get_or_create(
        caracteristica=caracteristicas_obj["Teclado"],
        tipo_dispositivo=tipos_dispositivo_obj["Teclado"], # Tipo de dispositivo "Teclado"
        interfaz_conexion="USB",
    )
    # Mouse - Conectividad Bluetooth, Característica "Mouse"
    CaracteristicaEspecifica.objects.get_or_create(
        caracteristica=caracteristicas_obj["Mouse"],
        tipo_dispositivo=tipos_dispositivo_obj["Mouse"], # Tipo de dispositivo "Mouse"
        interfaz_conexion="Bluetooth",
    )
    # Smartphone - RAM DDR5 8GB, Sistema Operativo Android
    CaracteristicaEspecifica.objects.get_or_create(
        caracteristica=caracteristicas_obj["RAM"],
        tipo_dispositivo=tipos_dispositivo_obj["Smartphone"],
        tipo_memoria=tipos_memoria_obj["DDR5"],
        cantidad_memoria=cantidades_memoria_obj[8],
    )
    CaracteristicaEspecifica.objects.get_or_create(
        caracteristica=caracteristicas_obj["Sistema Operativo"],
        tipo_dispositivo=tipos_dispositivo_obj["Smartphone"],
        tipo_procesador="Android", # Usando tipo_procesador para Sistema Operativo
    )


    # --- 3. Usuarios, Gerencias y Grupos ---
    print("Poblando usuarios y gerencias...")

    gerencia_informatica = gerencias_obj["Informática"] # Usar objetos del diccionario
    gerencia_administracion = gerencias_obj["Administración"] # Usar objetos del diccionario
    gerencia_ventas = gerencias_obj["Ventas"] # Nueva gerencia

    # Crear grupos (roles) - Ejemplo: "Agentes de Inventario", "Usuarios Generales"
    grupo_agentes_inventario, created = Group.objects.get_or_create(name="Agentes de Inventario")
    grupo_usuarios_generales, created = Group.objects.get_or_create(name="Usuarios Generales") # Nuevo grupo

    # Crear usuarios
    usuario_admin = CustomUser.objects.create_superuser(username='admin', password='admin123', email='admin@example.com', first_name='Admin', last_name='User')
    usuario_admin.gerencia = gerencia_informatica
    usuario_admin.is_staff = True
    usuario_admin.is_active = True
    usuario_admin.save()

    usuario_agente1 = CustomUser.objects.create_user(username='agente1', password='agente123', email='agente1@example.com', first_name='Agente', last_name='Uno')
    usuario_agente1.gerencia = gerencia_informatica
    usuario_agente1.is_staff = True
    usuario_agente1.is_active = True
    usuario_agente1.groups.add(grupo_agentes_inventario)
    usuario_agente1.save()

    usuario_usuario1 = CustomUser.objects.create_user(username='usuario1', password='usuario123', email='usuario1@example.com', first_name='Usuario', last_name='Uno')
    usuario_usuario1.gerencia = gerencia_administracion
    usuario_usuario1.is_staff = False
    usuario_usuario1.is_active = True
    usuario_usuario1.groups.add(grupo_usuarios_generales) # Añadir a "Usuarios Generales"
    usuario_usuario1.save()

    usuario_usuario2 = CustomUser.objects.create_user(username='usuario2', password='usuario2123', email='usuario2@example.com', first_name='Usuario', last_name='Dos') # Nuevo usuario
    usuario_usuario2.gerencia = gerencia_ventas # Nueva gerencia para usuario2
    usuario_usuario2.is_staff = False
    usuario_usuario2.is_active = True
    usuario_usuario2.groups.add(grupo_usuarios_generales) # También "Usuarios Generales"
    usuario_usuario2.save()

    usuario_inactivo = CustomUser.objects.create_user(username='inactivo', password='inactivo123', email='inactivo@example.com', first_name='Usuario', last_name='Inactivo', is_active=False)
    usuario_inactivo.gerencia = gerencia_administracion
    usuario_inactivo.is_staff = False
    usuario_inactivo.save()


    # --- 4. Marcas y Modelos (¡Importante: Marcas antes que Modelos!) ---
    print("Poblando marcas y modelos...")

    marca_lenovo = marcas_obj["Lenovo"] # Usar objetos del diccionario (¡Asegúrate de que Marca Lenovo se crea ANTES!)
    marca_hp = marcas_obj["HP"] # Usar objetos del diccionario
    marca_dell = marcas_obj["Dell"] # Usar objetos del diccionario
    marca_apple = marcas_obj["Apple"] # Usar objetos del diccionario
    marca_samsung = marcas_obj["Samsung"] # Usar objetos del diccionario
    marca_logitech = marcas_obj["Logitech"] # Usar objetos del diccionario
    marca_microsoft = marcas_obj["Microsoft"] # Usar objetos del diccionario
    marca_xiaomi = marcas_obj["Xiaomi"] # Usar objetos del diccionario
    marca_brother = marcas_obj["Brother"] # Usar objetos del diccionario


    # Modelos Lenovo (Notebooks)
    Modelo.objects.get_or_create(nombre="ThinkPad T480", marca_id_marca=marca_lenovo)
    Modelo.objects.get_or_create(nombre="ThinkPad X1 Carbon", marca_id_marca=marca_lenovo)
    Modelo.objects.get_or_create(nombre="IdeaPad 3", marca_id_marca=marca_lenovo)

    # Modelos HP (Notebooks y Monitores)
    Modelo.objects.get_or_create(nombre="EliteBook 840 G7", marca_id_marca=marca_hp)
    Modelo.objects.get_or_create(nombre="ProBook 450 G8", marca_id_marca=marca_hp)
    Modelo.objects.get_or_create(nombre="E24 G4 Monitor", marca_id_marca=marca_hp)

    # Modelos Dell (Notebooks y Monitores)
    Modelo.objects.get_or_create(nombre="XPS 13", marca_id_marca=marca_dell)
    Modelo.objects.get_or_create(nombre="Latitude 5420", marca_id_marca=marca_dell)
    Modelo.objects.get_or_create(nombre="UltraSharp U2722D Monitor", marca_id_marca=marca_dell)

    # Modelos Apple (Notebooks y Tablets)
    Modelo.objects.get_or_create(nombre="MacBook Air M1", marca_id_marca=marca_apple)
    Modelo.objects.get_or_create(nombre="iPad Pro 12.9", marca_id_marca=marca_apple)

    # Modelos Samsung (Smartphones y Tablets)
    Modelo.objects.get_or_create(nombre="Galaxy S21", marca_id_marca=marca_samsung)
    Modelo.objects.get_or_create(nombre="Galaxy Tab S7", marca_id_marca=marca_samsung)

    # Modelos Logitech (Mouses y Teclados)
    Modelo.objects.get_or_create(nombre="MX Master 3 Mouse", marca_id_marca=marca_logitech)
    Modelo.objects.get_or_create(nombre="MX Keys Teclado", marca_id_marca=marca_logitech)

    # Modelos Microsoft (Notebooks y Mouses)
    Modelo.objects.get_or_create(nombre="Surface Laptop 4", marca_id_marca=marca_microsoft)
    Modelo.objects.get_or_create(nombre="Surface Mouse", marca_id_marca=marca_microsoft)

    # Modelos Xiaomi (Smartphones)
    Modelo.objects.get_or_create(nombre="Mi 11", marca_id_marca=marca_xiaomi)

    # Modelos Brother (Impresoras)
    Modelo.objects.get_or_create(nombre="HL-L2350DW Impresora", marca_id_marca=marca_brother)


    # --- 5. Dispositivos (Ejemplos Más Variados) ---
    print("Poblando dispositivos...")

    tipo_notebook = tipos_dispositivo_obj["Notebook"] # Usar objetos del diccionario
    tipo_monitor = tipos_dispositivo_obj["Monitor"] # Usar objetos del diccionario
    tipo_smartphone = tipos_dispositivo_obj["Smartphone"] # Nuevo tipo
    tipo_teclado = tipos_dispositivo_obj["Teclado"] # Usar objetos del diccionario
    tipo_mouse = tipos_dispositivo_obj["Mouse"] # Usar objetos del diccionario
    tipo_impresora = tipos_dispositivo_obj["Impresora"] # Nuevo tipo

    estado_disponible = estados_dispositivo_obj["Disponible"] # Usar objetos del diccionario
    estado_en_uso = estados_dispositivo_obj["En uso"] # Usar objetos del diccionario
    estado_en_reparacion = estados_dispositivo_obj["En reparación"] # Nuevo estado

    ubicacion_casa_central_1 = ubicaciones_obj["Casa Central-1"] # Usar objetos del diccionario (clave más descriptiva)
    ubicacion_casa_central_2 = ubicaciones_obj["Casa Central-2"] # Usar objetos del diccionario
    ubicacion_sucursal_norte_pb = ubicaciones_obj["Sucursal Norte-Planta Baja"] # Usar objetos del diccionario
    ubicacion_deposito = ubicaciones_obj["Depósito-Único"] # Nueva ubicación


    usuario_agente1 = CustomUser.objects.get(username="agente1") # Usar get para obtener usuarios
    usuario_usuario1 = CustomUser.objects.get(username="usuario1") # Usar get para obtener usuarios
    usuario_usuario2 = CustomUser.objects.get(username="usuario2") # Usar get para obtener usuarios

    modelo_thinkpad_t480 = Modelo.objects.get(nombre="ThinkPad T480", marca_id_marca=marca_lenovo) # ¡Ahora debería existir!
    modelo_elitebook_840_g7 = Modelo.objects.get(nombre="EliteBook 840 G7", marca_id_marca=marca_hp) # Nuevo modelo
    modelo_ultrasharp_u2722d = Modelo.objects.get(nombre="UltraSharp U2722D Monitor", marca_id_marca=marca_dell) # Nuevo modelo
    modelo_mx_master_3_mouse = Modelo.objects.get(nombre="MX Master 3 Mouse", marca_id_marca=marca_logitech) # Nuevo modelo
    modelo_mi_11 = Modelo.objects.get(nombre="Mi 11", marca_id_marca=marca_xiaomi) # Nuevo modelo
    modelo_hl_l2350dw_impresora = Modelo.objects.get(nombre="HL-L2350DW Impresora", marca_id_marca=marca_brother) # Nuevo modelo


    # Dispositivo 1: Notebook Lenovo ThinkPad T480, Agente1, Casa Central 1, En Uso
    dispositivo1 = Dispositivo.objects.create(
        nomenclatura="NOTE-001",
        tipo_dispositivo=tipo_notebook,
        propietario=usuario_agente1,
        serie="SERIE-NOTE-001",
        jira="JIRA-1234",
    )
    DispositivoEstado.objects.create(dispositivo_id_dispositivo=dispositivo1, fecha=datetime.date.today(), estado_id_estado=estado_en_uso, comentario="Asignado a Agente 1", agente=usuario_admin) # Registro de estado inicial
    DispositivoUbicacion.objects.create(dispositivo_id_dispositivo=dispositivo1, fecha=datetime.date.today(), ubicacion_id_ubicacion=ubicacion_casa_central_1, comentario="Ubicado en oficina Agente 1", agente=usuario_admin) # Registro de ubicación inicial
    DispositivoPropietarioHistorico.objects.create(dispositivo=dispositivo1, propietario_id_nuevo=usuario_agente1, fecha_cambio=timezone.now(), comentario="Asignación inicial", agente=usuario_admin) # Registro de propietario histórico inicial

    # Dispositivo 2: Monitor Dell UltraSharp, Usuario1, Sucursal Norte PB, Disponible
    dispositivo2 = Dispositivo.objects.create(
        nomenclatura="MONITOR-001",
        tipo_dispositivo=tipo_monitor,
        propietario=usuario_usuario1,
        serie="SERIE-MONITOR-001",
        jira="JIRA-5678",
    )
    DispositivoEstado.objects.create(dispositivo_id_dispositivo=dispositivo2, fecha=datetime.date.today(), estado_id_estado=estado_disponible, comentario="Ingreso al inventario", agente=usuario_agente1) # Registro de estado inicial
    DispositivoUbicacion.objects.create(dispositivo_id_dispositivo=dispositivo2, fecha=datetime.date.today(), ubicacion_id_ubicacion=ubicacion_sucursal_norte_pb, comentario="Ubicado en Sucursal Norte", agente=usuario_agente1) # Registro de ubicación inicial
    DispositivoPropietarioHistorico.objects.create(dispositivo=dispositivo2, propietario_id_nuevo=usuario_usuario1, fecha_cambio=timezone.now(), comentario="Asignación inicial a Usuario 1", agente=usuario_agente1) # Registro de propietario histórico inicial

    # Dispositivo 3: Notebook HP EliteBook, Usuario2, Casa Central 2, En Reparación
    dispositivo3 = Dispositivo.objects.create(
        nomenclatura="NOTE-002",
        tipo_dispositivo=tipo_notebook,
        propietario=usuario_usuario2,
        serie="SERIE-NOTE-002",
        jira="JIRA-9012",
    )
    DispositivoEstado.objects.create(dispositivo_id_dispositivo=dispositivo3, fecha=datetime.date.today(), estado_id_estado=estado_en_reparacion, comentario="Enviado a reparación por fallo de hardware", agente=usuario_agente1) # Registro de estado inicial
    DispositivoUbicacion.objects.create(dispositivo_id_dispositivo=dispositivo3, fecha=datetime.date.today(), ubicacion_id_ubicacion=ubicacion_casa_central_2, comentario="Retirado para reparación", agente=usuario_agente1) # Registro de ubicación inicial
    DispositivoPropietarioHistorico.objects.create(dispositivo=dispositivo3, propietario_id_nuevo=usuario_usuario2, fecha_cambio=timezone.now(), comentario="Asignación a Usuario 2", agente=usuario_agente1) # Registro de propietario histórico inicial

    # Dispositivo 4: Mouse Logitech MX Master 3, Agente1, Depósito, Disponible
    dispositivo4 = Dispositivo.objects.create(
        nomenclatura="MOUSE-001",
        tipo_dispositivo=tipo_mouse,
        propietario=usuario_agente1,
        serie="SERIE-MOUSE-001",
        jira="JIRA-3456",
    )
    DispositivoEstado.objects.create(dispositivo_id_dispositivo=dispositivo4, fecha=datetime.date.today(), estado_id_estado=estado_disponible, comentario="En stock en depósito", agente=usuario_admin) # Registro de estado inicial
    DispositivoUbicacion.objects.create(dispositivo_id_dispositivo=dispositivo4, fecha=datetime.date.today(), ubicacion_id_ubicacion=ubicacion_deposito, comentario="Almacenado en depósito", agente=usuario_admin) # Registro de ubicación inicial
    DispositivoPropietarioHistorico.objects.create(dispositivo=dispositivo4, propietario_id_nuevo=usuario_agente1, fecha_cambio=timezone.now(), comentario="Asignado a Agente 1 para pruebas", agente=usuario_admin) # Registro de propietario histórico inicial

    # Dispositivo 5: Smartphone Xiaomi Mi 11, Usuario2, Casa Central 2, En Uso
    dispositivo5 = Dispositivo.objects.create(
        nomenclatura="SMART-001",
        tipo_dispositivo=tipo_smartphone,
        propietario=usuario_usuario2,
        serie="SERIE-SMART-001",
        jira="JIRA-7890",
    )
    DispositivoEstado.objects.create(dispositivo_id_dispositivo=dispositivo5, fecha=datetime.date.today(), estado_id_estado=estado_en_uso, comentario="Smartphone personal de Usuario 2", agente=usuario_usuario2) # Registro de estado inicial (agente = usuario_usuario2 - ejemplo)
    DispositivoUbicacion.objects.create(dispositivo_id_dispositivo=dispositivo5, fecha=datetime.date.today(), ubicacion_id_ubicacion=ubicacion_casa_central_2, comentario="Usuario 2 lo tiene en su oficina", agente=usuario_usuario2) # Registro de ubicación inicial (agente = usuario_usuario2 - ejemplo)
    DispositivoPropietarioHistorico.objects.create(dispositivo=dispositivo5, propietario_id_nuevo=usuario_usuario2, fecha_cambio=timezone.now(), comentario="Asignación a Usuario 2 como móvil personal", agente=usuario_usuario2) # Registro de propietario histórico inicial (agente = usuario_usuario2 - ejemplo)

    # Dispositivo 6: Impresora Brother HL-L2350DW, Usuario1, Sucursal Norte PB, Disponible
    dispositivo6 = Dispositivo.objects.create(
        nomenclatura="IMPRESORA-001",
        tipo_dispositivo=tipo_impresora,
        propietario=usuario_usuario1,
        serie="SERIE-IMPRESORA-001",
        jira="JIRA-0001",
    )
    DispositivoEstado.objects.create(dispositivo_id_dispositivo=dispositivo6, fecha=datetime.date.today(), estado_id_estado=estado_disponible, comentario="Lista para ser instalada", agente=usuario_agente1) # Registro de estado inicial
    DispositivoUbicacion.objects.create(dispositivo_id_dispositivo=dispositivo6, fecha=datetime.date.today(), ubicacion_id_ubicacion=ubicacion_sucursal_norte_pb, comentario="Guardada en depósito de sucursal", agente=usuario_agente1) # Registro de ubicación inicial
    DispositivoPropietarioHistorico.objects.create(dispositivo=dispositivo6, propietario_id_nuevo=usuario_usuario1, fecha_cambio=timezone.now(), comentario="Asignada a Usuario 1 para pruebas de impresión", agente=usuario_agente1) # Registro de propietario histórico inicial

    print("¡Población de la base de datos COMPLETA!")