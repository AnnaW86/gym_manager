from db.run_sql import run_sql
from models.gym_class import GymClass
from repositories import class_type_repository, location_repository
from helpers.date_time_helper import all_start_times, off_peak_times

def save(gym_class):
    sql = """
        INSERT INTO gym_classes (class_type_id, start_time, duration, location_id, capacity)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING *    
    """
    values = [gym_class.class_type.id, gym_class.start_time, gym_class.duration, gym_class.location.id, gym_class.capacity]
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
        ORDER BY class_type_id, start_time
    """
    results = run_sql(sql)
    for row in results:
        class_type = class_type_repository.select(row['class_type_id'])
        location = location_repository.select(row['location_id'])
        gym_class = GymClass(class_type, row['start_time'], row['duration'],location, row['capacity'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def select_all_ordered_by_start_time():
    gym_classes = []
    sql = """
        SELECT * FROM gym_classes
        ORDER BY start_time
    """
    results = run_sql(sql)
    for row in results:
        class_type = class_type_repository.select(row['class_type_id'])
        location = location_repository.select(row['location_id'])
        gym_class = GymClass(class_type, row['start_time'], row['duration'],location, row['capacity'], row['id'])
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
        location = location_repository.select(result['location_id'])
        gym_class = GymClass(class_type, result['start_time'], result['duration'], location, result['capacity'], result['id'])
    return gym_class

def select_by_class_type_id(id):
    filtered_classes = []
    sql = """
        SELECT gym_classes.*
        FROM gym_classes
        INNER JOIN class_types
        ON class_types.id = gym_classes.class_type_id
        WHERE class_types.id = %s
        ORDER BY gym_classes.start_time
    """
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        class_type = class_type_repository.select(row['class_type_id'])
        location = location_repository.select(row['location_id'])
        filtered_class = GymClass(class_type, row['start_time'], row['duration'], location, row['capacity'], row['id'])
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
        ORDER BY gym_classes.start_time
    """
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        class_type = class_type_repository.select(row['class_type_id'])
        location = location_repository.select(row['location_id'])
        gym_class = GymClass(class_type, row['start_time'], row['duration'], location, row['capacity'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def update(gym_class):
    sql = """
        UPDATE gym_classes
        SET (class_type_id, start_time, duration, location_id, capacity) = (%s, %s, %s, %s, %s)
        WHERE id = %s
    """
    values = [gym_class.class_type.id, gym_class.start_time, gym_class.duration, gym_class.location.id, gym_class.capacity, gym_class.id]
    run_sql(sql, values)

def number_of_bookings(id):
    sql = """
        SELECT COUNT(*) FROM bookings
        WHERE gym_class_id = %s
    """
    values=[id]
    class_size = run_sql(sql, values)[0]['count']
    return class_size
    
def find_number_of_classes_scheduled(id):
    sql = """
        SELECT COUNT(*) FROM gym_classes
        WHERE class_type_id = %s
    """
    values = [id]
    number_of_classes = run_sql(sql, values)[0]['count']
    return number_of_classes

def find_available_class_times(id):
    available_class_times = []
    existing_bookings = class_type_repository.select_all_booked_times(id)
    for time in all_start_times:
        if time not in existing_bookings:
            available_class_times.append(time)
    return available_class_times

def available_places(gym_class):
    availability = gym_class.capacity - number_of_bookings(gym_class.id)
    return availability

def find_available_classes():
    all_gym_classes = select_all_ordered_by_start_time()
    available_classes = []
    for gym_class in all_gym_classes:
        if available_places(gym_class) > 0:
            available_classes.append(gym_class)
    return available_classes

def find_unbooked_classes(enrolled_gym_classes, available_classes):
    unbooked_classes = []
    for available_class in available_classes:
        booked = False
        for enrolled_class in enrolled_gym_classes:
            if available_class.id == enrolled_class.id:
                booked = True
        if booked == False:
            unbooked_classes.append(available_class)
    return unbooked_classes

def find_bookable_classes(member, unbooked_classes):
    bookable_classes = []
    if member.membership_type.title == 'premium':
        return unbooked_classes
    else:
        for unbooked_class in unbooked_classes:
            if unbooked_class.start_time in off_peak_times:
                bookable_classes.append(unbooked_class)
        return bookable_classes