from psycopg2 import Time
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

def select(id):
    time = None
    sql = """
        SELECT * FROM start_times
        WHERE id = %s
    """
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        time = StartTime(result['time'], result['id'])
    return time

def select_all():
    times = []
    sql = "SELECT * FROM start_times"
    results = run_sql(sql)
    for row in results:
        time = StartTime(row['time'], row['id'])
        times.append(time)
    return times

def select_all_ids():
    time_ids = []
    sql = "SELECT id FROM start_times"
    results = run_sql(sql)
    for row in results:
        time_ids.append(row['id'])
    return time_ids

def select_all_ids_for_class_type(id):
    times = []
    sql = """
        SELECT start_time_id FROM gym_classes
        WHERE class_type_id = %s
    """
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        times.append(row['start_time_id'])
    return times