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