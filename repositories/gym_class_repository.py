from db.run_sql import run_sql
from models.gym_class import GymClass
from repositories import class_type_repository, start_time_repository, location_repository

def save(gym_class):
    sql = """
        INSERT INTO gym_classes (class_type_id, start_time_id, duration, location_id, capacity)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING *    
    """
    values = [gym_class.class_type.id, gym_class.start_time.id, gym_class.duration, gym_class.location.id, gym_class.capacity]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)

def select_all():
    gym_classes = []
    sql = """
        SELECT * FROM gym_classes
        ORDER BY class_type_id
    """
    results = run_sql(sql)
    for row in results:
        class_type = class_type_repository.select(row['class_type_id'])
        start_time = start_time_repository.select(row['start_time_id'])
        location = location_repository.select(row['location_id'])
        gym_class = GymClass(class_type, start_time, row['duration'],location, row['capacity'], row['id'])
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
        gym_class = GymClass(class_type, start_time, result['duration'], location, result['capacity'], result['id'])
    return gym_class

def select_by_class_type_id(id):
    filtered_classes = []
    sql = """
        SELECT gym_classes.*
        FROM gym_classes
        INNER JOIN class_types
        ON class_types.id = gym_classes.class_type_id
        WHERE class_types.id = %s
        ORDER BY gym_classes.start_time_id
    """
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        class_type = class_type_repository.select(row['class_type_id'])
        start_time = start_time_repository.select(row['start_time_id'])
        location = location_repository.select(row['location_id'])
        filtered_class = GymClass(class_type, start_time, row['duration'], location, row['capacity'], row['id'])
        filtered_classes.append(filtered_class)
    return filtered_classes

def select_all_by_enrolled_member(id):
    gym_classes = []
    sql = """
        SELECT gym_classes.*
        FROM gym_classes
        INNER JOIN bookings
        ON bookings.gym_class_id =
        gym_classes.id
        WHERE bookings.member_id = %s 
        ORDER BY start_time_id
    """
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        class_type = class_type_repository.select(row['class_type_id'])
        start_time = start_time_repository.select(row['start_time_id'])
        location = location_repository.select(row['location_id'])
        gym_class = GymClass(class_type, start_time, row['duration'], location, row['capacity'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def check_class_size(id):
    sql = """
        SELECT COUNT(*) FROM bookings
        WHERE gym_class_id = %s
    """
    values=[id]
    class_size = run_sql(sql, values)[0]['count']
    return class_size

def find_class_times(id):
    booked_start_times_ids = []
    sql = """
        SELECT start_times_id FROM gym_classes
        WHERE id = %s
    """
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        booked_start_times_ids.append(row['start_time_id'])
    return booked_start_times_ids

def find_number_of_classes_scheduled(id):
    sql = """
        SELECT COUNT(*) FROM gym_classes
        WHERE class_type_id = %s
    """
    values = [id]
    number_of_classes = run_sql(sql, values)[0]['count']
    return number_of_classes