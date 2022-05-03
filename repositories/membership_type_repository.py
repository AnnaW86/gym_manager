from db.run_sql import run_sql
from models.membership_type import MembershipType

def save(membership_type):
    sql = """
        INSERT INTO membership_types (title)
        VALUES (%s)
        RETURNING *
    """
    values = [membership_type.title]
    results = run_sql(sql, values)
    membership_type.id = results[0]['id']
    return membership_type

def delete_all():
    sql = "DELETE FROM membership_types"
    run_sql(sql)

def select_all():
    membership_types = []
    sql = "SELECT * FROM membership_types"
    results = run_sql(sql)
    for row in results:
        membership_type = MembershipType(row['title'], row['id'])
        membership_types.append(membership_type)
    return membership_types

def select(id):
    membership_type = None
    sql = """
        SELECT * FROM membership_types
        WHERE id = %s
    """
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        membership_type = MembershipType(result['title'], result['id'])
    return membership_type

def select_from_type(type):
    membership_type = None
    sql = """
        SELECT * FROM membership_types
        WHERE title = %s
    """
    values = [type]
    result = run_sql(sql, values)[0]
    if result is not None:
        membership_type = MembershipType(result['title'], result['id'])
    return membership_type