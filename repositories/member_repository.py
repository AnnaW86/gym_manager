from db.run_sql import run_sql
from models.member import Member
from repositories import membership_type_repository

def save(member):
    sql = """
        INSERT INTO members (first_name, last_name, membership_number, membership_type_id, active_status)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING *
    """
    values = [member.first_name, member.last_name, member.membership_number, member.membership_type.id, member.active_status]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def select_all():
    members = []
    sql = """
        SELECT * FROM members
        ORDER BY last_name
    """
    results = run_sql(sql)
    for row in results:
        membership_type = membership_type_repository.select(row['membership_type_id'])
        member = Member(row['first_name'], row['last_name'], row['membership_number'], membership_type, row['active_status'], row['id'])
        members.append(member)
    return members

def select_all_active():
    members = []
    sql = """
        SELECT * FROM members
        WHERE active_status = True
        ORDER BY last_name
    """
    results = run_sql(sql)
    for row in results:
        membership_type = membership_type_repository.select(row['membership_type_id'])
        member = Member(row['first_name'], row['last_name'], row['membership_number'], membership_type, row['active_status'], row['id'])
        members.append(member)
    return members

def select_all_by_deactivated():
    members = []
    sql = """
        SELECT * FROM members
        WHERE active_status = False
        ORDER BY last_name
    """
    results = run_sql(sql)
    for row in results:
        membership_type = membership_type_repository.select(row['membership_type_id'])
        member = Member(row['first_name'], row['last_name'], row['membership_number'], membership_type, row['active_status'], row['id'])
        members.append(member)
    return members


def update(member):
    sql = """
        UPDATE members
        SET (first_name, last_name, membership_number, membership_type_id, active_status) = (%s, %s, %s, %s, %s)
        WHERE id = %s
    """
    values = [member.first_name, member.last_name, member.membership_number, member.membership_type.id, member.active_status, member.id]
    run_sql(sql, values)

def select(id):
    member = None
    sql = """
        SELECT * FROM members
        WHERE id = %s
    """
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        membership_type = membership_type_repository.select(result['membership_type_id'])
        member = Member(result['first_name'], result['last_name'], result['membership_number'], membership_type, result['active_status'], result['id'])
    return member

def select_all_by_gym_class(id):
    members = []
    sql = """
        SELECT members.*
        FROM members
        INNER JOIN bookings
        ON bookings.member_id =
        members.id
        WHERE bookings.gym_class_id = %s 
    """
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        membership_type = membership_type_repository.select(row['membership_type_id'])
        member = Member(row['first_name'], row['last_name'], row['membership_number'], membership_type, row['active_status'], row['id'])
        members.append(member)
    return members

def find_number_of_attendees(id):
    sql = """
        SELECT COUNT(*)
        FROM members
        INNER JOIN bookings
        ON bookings.member_id = members.id
        WHERE bookings.gym_class_id = %s
    """
    values = [id]
    number_of_attendees = run_sql(sql, values)[0]['count']
    return number_of_attendees


def find_available_places(id):
    sql = """
        SELECT COUNT(*) FROM bookings
        WHERE member_id = %s 
    """
    values = [id]
    available_places = run_sql(sql, values)[0]['count']
    return available_places
