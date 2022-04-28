from cProfile import run
from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = """
        INSERT INTO members (first_name, last_name, membership_number)
        VALUES (%s, %s, %s)
        RETURNING *
    """
    values = [member.first_name, member.last_name, member.membership_number]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['membership_number'], row['id'])
        members.append(member)
    return members

def update(member):
    sql = """
        UPDATE members
        SET (first_name, last_name, membership_number) = (%s, %s, %s)
        WHERE id = %s
    """
    values = [member.first_name, member.last_name, member.membership_number, member.id]
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
        member = Member(result['first_name'], result['last_name'], result['membership_number'], result['id'])
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
        member = Member(row['first_name'], row['last_name'], row['membership_number'], row['id'])
        members.append(member)
    return members
