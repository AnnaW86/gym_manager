from db.run_sql import run_sql

from models.class_type import ClassType

def save(class_type):
    sql = """
        INSERT INTO class_types (title, intensity, description)
        VALUES (%s, %s, %s)
        RETURNING *
    """
    values = [class_type.title, class_type.intensity, class_type.description]
    results = run_sql(sql, values)
    class_type.id = results[0]['id']
    return class_type

def delete_all():
    sql = "DELETE FROM class_types"
    run_sql(sql)

def select_all():
    class_types = []
    sql = "SELECT * FROM class_types"
    results = run_sql(sql)
    for row in results:
        class_type = ClassType(row['title'], row['intensity'], row['description'], row['id'])
        class_types.append(class_type)
    return class_types