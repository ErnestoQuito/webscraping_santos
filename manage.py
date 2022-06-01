import argparse

def main():
    from scripts.modulos.models import meta 
    from scripts.modulos.db import MSSQL
    from scripts.modulos.setting import get_setting

    parse = argparse.ArgumentParser()
    parse.add_argument(
        'creartablas',
        help='Comando para crear las tablas del archivo models'
    )
    args = parse.parse_args()

    if args.creartablas == 'creartablas':
        
        creadentials = get_setting('db.ini', 'BASEDATOS')
        mssql = MSSQL()
        mssql.host = creadentials['host']
        mssql.name = creadentials['name']
        mssql.user = creadentials['user']
        mssql.password = creadentials['password']
        mssql.driver_engine = creadentials['driver_engine']
        engine = mssql.engine()
        meta.create_all(engine)

if __name__ == '__main__':
    main()
