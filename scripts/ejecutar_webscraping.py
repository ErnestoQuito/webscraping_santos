import time
import sys
import logging
from datetime import datetime
from modulos.reniec_selenium import Reniec
from modulos.setting import get_setting
from modulos.reniec_personas import ReniecPersonas
from modulos.reniec_bases import ReniecBases


# Establecer Loggin
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(process)d - %(message)s',
    level=logging.INFO,
    filename='reniec_selenium.log',
    filemode='a'
)
# Establcer nombre de columnas
nombre_campos_personales = (
    'dni', 'dig_verificador', 'ciudadano', 'edad',
    'genero', 'domicilio_ubigeo_1', 'domicilio_ubigeo_2', 'domicilio_ubigeo_3',
    'domicilio', 'codigo_postal', 'direccion_jr_av_ci', 'direccion_nombre',
    'numero', 'Bio_cha', 'dpto_piso', 'urb_condominio', 'etapa', 'mz', 'lote',
    'naci_ubideo_1', 'naci_ubigeo_2',  'naci_ubigeo_3', 'naci_direccion', 'fecha_nacimiento',
    'estado_civil', 'grado_instituto', 'estatura', 'genero2', 'grupo_votacion',
    'dona_organos', 'fecha_inscripcion', 'fecha_emision', 'fecha_caducidad',
    'ficha', 'n_imagen', 'fecha_actualizacion', 'multas_electorales',
    'doc_sustento', 'multa_administrativa', 'num_doc_sustento', 'restriccion',
    'fecha_restriccion', 'interdiccion', 'discapacidad', 'desconocido1',
    'desconocido2', 'desconocido3', 'desconocido4', 'desconocido5', 'desconocido6',
    'desconocido7', 'desconocido8', 'desconocido9', 'desconocido10', 'desconocido11',
)

nombre_campos_padres = ('padre_pri_apellido', 'padre_seg_apellido', 'padre_nombre', 'padre_tip_doc',
    'padre_num_docu', 'madre_pri_apellido', 'madre_seg_apellido', 'madre_nombre',
    'madre_tip_doc', 'madre_num_doc', 'otro_tele', 'otro_correo'
)
# credenciales
setting_credentials = get_setting('reniec.ini', 'RENIEC')
# Instancia Tabla
reniec_personas = ReniecPersonas()
reniec_personas.abrir_engine()
# Instancia de tabla reniec_bases
reniec_bases = ReniecBases()
reniec_bases.abrir_engine()
# Instancia Selenium Personalizado para Reniec
reniec = Reniec()
try:
    # Metodos Selenium
    reniec.link = setting_credentials['link']
    reniec.abrir_web()
    reniec.establacer_user(setting_credentials['user'])
    reniec.establecer_password(setting_credentials['password'])
    reniec.acceder()
    # Recorrer Bases
    reniec_bases_df = reniec_bases.obtener_top_bases()
    for filas in reniec_bases_df.itertuples():
        reniec.ingresar_documento(filas[2])
        reniec.buscar_documento()
        # Obtener datos de la Reniec
        time.sleep(3)
        encontro_documento = reniec.existe_documento()
        if encontro_documento:
            campos = reniec.obtener_campos()
            valores = []
            data_pers_dict = {}
            for i, c in enumerate(campos[1:]):
                data_pers_dict[nombre_campos_personales[i]] = c.get_attribute('value')
            reniec.ir_datos_padres()
            campos = reniec.obtener_campos()
            time.sleep(1)
            # Raspado web
            valores = []
            data_padre_dict = {}
            for i, c in enumerate(campos[6:18]):
                data_padre_dict[nombre_campos_padres[i]] = c.get_attribute('value')
            data_pers_dict.update(data_padre_dict)
            # Limpiar valores a nullos
            for i in data_pers_dict:
                if len(data_pers_dict[i]) == 0:
                    data_pers_dict[i] = None
            # print(data_pers_dict)
            # Dar formato a las fechas
            if data_pers_dict['fecha_nacimiento']:
                data_pers_dict['fecha_nacimiento'] = datetime.strptime(
                    data_pers_dict['fecha_nacimiento'], '%d/%m/%Y'
                )
            if data_pers_dict['fecha_inscripcion']:
                data_pers_dict['fecha_inscripcion'] = datetime.strptime(
                    data_pers_dict['fecha_inscripcion'], '%d/%m/%Y'
                )
            if data_pers_dict['fecha_emision']:
                data_pers_dict['fecha_emision'] = datetime.strptime(
                    data_pers_dict['fecha_emision'], '%d/%m/%Y'
                )
            if data_pers_dict['fecha_caducidad']:
                data_pers_dict['fecha_caducidad'] = datetime.strptime(
                    data_pers_dict['fecha_caducidad'], '%d/%m/%Y'
                )
            if data_pers_dict['fecha_actualizacion']:
                data_pers_dict['fecha_actualizacion'] = datetime.strptime(
                    data_pers_dict['fecha_actualizacion'], '%d/%m/%Y'
                )
            if data_pers_dict['fecha_restriccion']:
                data_pers_dict['fecha_restriccion'] = datetime.strptime(
                    data_pers_dict['fecha_restriccion'], '%d/%m/%Y'
                )
            # Insertar
            reniec_personas.insert(data_pers_dict)
            reniec_bases.actualizar_tabla(
                { 'id_base': filas[1], 'observacion': 'encontrado' }
            )
            reniec.ir_nueva_consulta()
        else:
            reniec_bases.actualizar_tabla(
                { 'id_base': filas[1], 'observacion': 'No se encontró registro' }
            )
except Exception:
    print(sys.exc_info())
    logging.error(sys.exc_info)
finally:
    time.sleep(10)
    reniec_personas.cerrar_engine()
    reniec_bases.cerrar_engine()
    reniec.cerrar_web()
