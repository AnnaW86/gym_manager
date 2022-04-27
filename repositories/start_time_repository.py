from db.run_sql import run_sql
from models.start_time import StartTime

def save(time):
    sql = """
        INSERT INTO start_times (time)
        VALUES (%s)
        RETURNING *
    """
    values = [time.time]
    results = run_sql(sql, values)
    time.id = results[0]['id']
    return time

def delete_all():
    sql = "DELETE FROM start_times"
    run_sql(sql)