from db.run_sql import run_sql
from models.gym_class import GymClass
from repositories import class_type_repository, start_time_repository, location_repository

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

def select_all():
    gym_classes = []
    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)
    for row in results:
        class_type = class_type_repository.select(row['class_type_id'])
        start_time = start_time_repository.select(row['start_time_id'])
        location = location_repository.select(row['location_id'])
        gym_class = GymClass(class_type, start_time, row['duration'],location, row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def select(id):
    gym_class = None
    sql = """
        SELECT * FROM gym_classes
        WHERE id = %s
    """
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        class_type = class_type_repository.select(result['class_type_id'])
        start_time = start_time_repository.select(result['start_time_id'])
        location = location_repository.select(result['location_id'])
        gym_class = GymClass(class_type, start_time, result['duration'], location, result['id'])
    return gym_class
