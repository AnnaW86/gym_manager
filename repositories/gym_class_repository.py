from db.run_sql import run_sql
from models.gym_class import GymClass

def save(gym_class):
    sql = """
        INSERT INTO gym_classes (class_type_id, start_time_id, duration, location_id)
        VALUES (%s, %s, %s, %s)
        RETURNING *    
    """
    values = [gym_class.class_type.id, gym_class.start_time.id, gym_class.duration, gym_class.location.id]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)
