from db.run_sql import run_sql
from models.location import Location

def save(location):
    sql = """
        INSERT INTO locations (name)
        VALUES (%s)
        RETURNING *
    """
    values = [location.name]
    results = run_sql(sql, values)
    location.id = results[0]['id']
    return location

def delete_all():
    sql = "DELETE FROM locations"
    run_sql(sql)