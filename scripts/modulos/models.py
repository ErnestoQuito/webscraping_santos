from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import Date
from sqlalchemy import BigInteger

meta = MetaData()

reniec_personas = Table(
    'reniec_personas',
    meta,
    Column('dni', String(length=10)),
    Column('dig_verificador', String(10), nullable=True),
    Column('ciudadano', String(250), nullable=True),
    Column('edad', String(10), nullable=True),
    Column('genero', String(length=50), nullable=True),
    Column('domicilio_ubigeo_1', String(10), nullable=True),
    Column('domicilio_ubigeo_2', String(10), nullable=True),
    Column('domicilio_ubigeo_3', String(10), nullable=True),
    Column('domicilio', String(length=250), nullable=True),
    Column('codigo_postal', String(10), nullable=True),
    Column('direccion_jr_av_ci', String(length=250), nullable=True),
    Column('direccion_nombre', String(length=250), nullable=True),
    Column('numero', String(10), nullable=True),
    Column('Bio_cha', String(length=250), nullable=True),
    Column('dpto_piso', String(length=250), nullable=True),
    Column('urb_condominio', String(length=250), nullable=True),
    Column('etapa', String(length=250), nullable=True),
    Column('mz', String(length=250), nullable=True),
    Column('lote', String(length=250), nullable=True),
    Column('naci_ubideo_1', String(10), nullable=True),
    Column('naci_ubigeo_2', String(10), nullable=True),
    Column('naci_ubigeo_3', String(10), nullable=True),
    Column('naci_direccion', String(length=250), nullable=True),
    Column('fecha_nacimiento', Date, nullable=True),
    Column('estado_civil', String(length=250), nullable=True),
    Column('grado_instituto', String(length=250), nullable=True),
    Column('estatura', String(10), nullable=True),
    Column('genero2', String(length=250), nullable=True),
    Column('grupo_votacion', String(length=250), nullable=True),
    Column('dona_organos', String(length=250), nullable=True),
    Column('fecha_inscripcion', Date, nullable=True),
    Column('fecha_emision', Date, nullable=True),
    Column('fecha_caducidad', Date, nullable=True),
    Column('ficha', Integer, nullable=True),
    Column('n_imagen', Integer, nullable=True),
    Column('fecha_actualizacion', Date, nullable=True),
    Column('multas_electorales', String(length=250), nullable=True),
    Column('doc_sustento', String(length=250), nullable=True),
    Column('multa_administrativa', String(length=250), nullable=True),
    Column('num_doc_sustento', String(length=250), nullable=True),
    Column('restriccion', String(length=250), nullable=True),
    Column('fecha_restriccion', Date, nullable=True),
    Column('interdiccion', String(length=250), nullable=True),
    Column('discapacidad', String(length=250), nullable=True),
    Column('observaciones', String(length=250), nullable=True),
    Column('glosa_informativa', String(length=250), nullable=True),
    Column('padre_pri_apellido', String(length=250), nullable=True),
    Column('padre_seg_apellido', String(length=250), nullable=True),
    Column('padre_nombre', String(length=250), nullable=True),
    Column('padre_tip_doc', String(length=250), nullable=True),
    Column('padre_num_docu', String(length=10), nullable=True),
    Column('madre_pri_apellido', String(length=250), nullable=True),
    Column('madre_seg_apellido', String(length=250), nullable=True),
    Column('madre_nombre', String(length=250), nullable=True),
    Column('madre_tip_doc', String(length=250), nullable=True),
    Column('madre_num_doc', String(length=10), nullable=True),
    Column('otro_tele', String(length=250), nullable=True),
    Column('otro_correo', String(length=250), nullable=True),
    Column('foto_persona', Text, nullable=True),
    Column('foto_huella_1', Text, nullable=True),
    Column('foto_huella_2', Text, nullable=True),
    Column('foto_firma', Text, nullable=True),
    
)

reniec_base = Table(
    'reniec_bases',
    meta,
    Column('id_base', BigInteger, primary_key=True, autoincrement=True),
    Column('documento', String(10), nullable=True),
    Column('observacion', String(250), nullable=True)
)
