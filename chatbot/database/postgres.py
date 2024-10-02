import json

from sqlalchemy import MetaData, create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text


def get_database_schema():
    with open("config.json", "r") as f:
        data = json.load(f)
    connection_string = data["db_uri"]

    engine = create_engine(connection_string)
    metadata = MetaData()
    metadata.reflect(bind=engine)

    schema_info = ""
    for table_name, table in metadata.tables.items():
        schema_info += f"Tabla: {table_name} "
        schema_info += "Columnas: "
        for column in table.columns:
            schema_info += f" {column.name}: {column.type}"
        schema_info += " "

    return schema_info.strip()


def execute_sql(input: str):
    with open("config.json", "r") as f:
        data = json.load(f)
    connection_string = data["db_uri"]

    engine = create_engine(connection_string)
    session = sessionmaker(bind=engine)
    Session = session()

    sql_text = text(input)
    result = Session.execute(sql_text)
    column_names = result.keys()

    data = []
    i = 0
    lista=[]
    for j in result:
        lista.append(list(j))
    for column in column_names:
        data_dict = { "column": column, "values": []}
        for row in lista:
            data_dict['values'].append(row[i])
        i += 1 
        data.append(data_dict)
    return data