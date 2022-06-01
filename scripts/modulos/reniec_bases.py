from sqlalchemy import update
from .db import MSSQL
from .setting import get_setting
from .models import reniec_base

class ReniecBases(MSSQL):
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

    def actualizar_tabla(self, documentos: dict):
        stm = (
            update(reniec_base).where(
                reniec_base.c.id_base == documentos['id_base']
            ).values(observacion=documentos['observacion'])
        )

        self.engine_connect.execute(stm)

    def obtener_top_bases(self, top: int = 50):
        import pandas as pd
        
        resultado = pd.read_sql(
            f"SELECT TOP {top} * FROM [reniec_bases] WHERE observacion != 'encontrado' OR observacion is NULL",
            self.engine()
        )
        
        return resultado

    def cerrar_engine(self):
        if self.engine_connect:
            self.engine_connect.close()
