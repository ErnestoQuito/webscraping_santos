from sqlalchemy import insert
from .db import MSSQL
from .setting import get_setting
from .models import reniec_personas


class ReniecPersonas(MSSQL):
    engine_connect = None

    def __init__(self) -> None:
        credentials = get_setting('db.ini', 'BASEDATOS')
        self.host = credentials['host']
        self.name = credentials['name']
        self.user = credentials['user']
        self.password = credentials['password']
        self.driver_engine = credentials['driver_engine']
    
    def abrir_engine(self):
        self.engine_connect = self.engine().connect()
    
    def insert(self, personas: dict):
        stm = (
            insert(reniec_personas).values(
                dni=personas['dni'],
                dig_verificador=personas['dig_verificador'],
                ciudadano=personas['ciudadano'],
                edad=personas['edad'],
                genero=personas['genero'],
                domicilio_ubigeo_1=personas['domicilio_ubigeo_1'],
                domicilio_ubigeo_2=personas['domicilio_ubigeo_2'],
                domicilio_ubigeo_3=personas['domicilio_ubigeo_3'],
                domicilio=personas['domicilio'],
                codigo_postal=personas['codigo_postal'],
                direccion_jr_av_ci=personas['direccion_jr_av_ci'],
                direccion_nombre=personas['direccion_nombre'],
                numero=personas['numero'],
                Bio_cha=personas['Bio_cha'],
                dpto_piso=personas['dpto_piso'],
                urb_condominio=personas['urb_condominio'],
                etapa=personas['etapa'],
                mz=personas['mz'],
                lote=personas['lote'],
                naci_ubideo_1=personas['naci_ubideo_1'],
                naci_ubigeo_2=personas['naci_ubigeo_2'],
                naci_ubigeo_3=personas['naci_ubigeo_3'],
                naci_direccion=personas['naci_direccion'],
                fecha_nacimiento=personas['fecha_nacimiento'],
                estado_civil=personas['estado_civil'],
                grado_instituto=personas['grado_instituto'],
                estatura=personas['estatura'],
                genero2=personas['genero2'],
                grupo_votacion=personas['grupo_votacion'],
                dona_organos=personas['dona_organos'],
                fecha_inscripcion=personas['fecha_inscripcion'],
                fecha_emision=personas['fecha_emision'],
                fecha_caducidad=personas['fecha_caducidad'],
                ficha=personas['ficha'],
                n_imagen=personas['n_imagen'],
                fecha_actualizacion=personas['fecha_actualizacion'],
                multas_electorales=personas['multas_electorales'],
                doc_sustento=personas['doc_sustento'],
                multa_administrativa=personas['multa_administrativa'],
                num_doc_sustento=personas['num_doc_sustento'],
                restriccion=personas['restriccion'],
                fecha_restriccion=personas['fecha_restriccion'],
                interdiccion=personas['interdiccion'],
                discapacidad=personas['discapacidad'],
                foto_persona=personas['foto_persona'],
                foto_huella_1=personas['foto_huella_1'],
                foto_huella_2=personas['foto_huella_2'],
                foto_firma=personas['foto_firma'],
                padre_pri_apellido=personas['padre_pri_apellido'],
                padre_seg_apellido=personas['padre_seg_apellido'],
                padre_nombre=personas['padre_nombre'],
                padre_tip_doc=personas['padre_tip_doc'],
                padre_num_docu=personas['padre_num_docu'],
                madre_pri_apellido=personas['madre_pri_apellido'],
                madre_seg_apellido=personas['madre_seg_apellido'],
                madre_nombre=personas['madre_nombre'],
                madre_tip_doc=personas['madre_tip_doc'],
                madre_num_doc=personas['madre_num_doc'],
                otro_tele=personas['otro_tele'],
                otro_correo=personas['otro_correo']
            )
        )
        
        self.engine_connect.execute(stm)
    
    def cerrar_engine(self):
        if self.engine_connect:
            self.engine_connect.close()
        