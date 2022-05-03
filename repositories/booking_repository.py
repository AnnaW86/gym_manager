from db.run_sql import run_sql
from models.booking import Booking
from repositories import member_repository, gym_class_repository

def save(booking):
    sql = """
        INSERT INTO bookings (member_id, gym_class_id)
        VALUES (%s, %s)
        RETURNING *
    """
    values = [booking.member.id, booking.gym_class.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = """
        DELETE FROM bookings
        WHERE member_id = %s
    """
    values = [id]
    run_sql(sql, values)

def delete_all_by_member_id(id):
    sql =  "DELETE FROM bookings WHERE member_id = %s"
    values = [id]
    run_sql(sql, values)