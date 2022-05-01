from db.run_sql import run_sql
from models.membership_type import MembershipType

def save(membership_type):
    sql = """
        INSERT INTO membership_types (membership_type)
        VALUES (%s)
        RETURNING *
    """
    values = [membership_type.membership_type]
    results = run_sql(sql, values)
    membership_type.id = results[0]['id']
    return membership_type

def delete_all():
    sql = "DELETE FROM membership_types"
    run_sql(sql)