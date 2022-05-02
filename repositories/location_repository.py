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

def select(id):
    location = None
    sql = """
        SELECT * FROM locations
        WHERE id = %s
    """
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        location = Location(result['name'], result['id'])
    return location

def select_all():
    locations = []
    sql = """SELECT * FROM locations
        ORDER BY name
    """
    results = run_sql(sql)
    for row in results:
        location = Location(row['name'], row['id'])
        locations.append(location)
    return locations

