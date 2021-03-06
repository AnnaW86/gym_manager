from flask import Blueprint, request, redirect

from models.booking import Booking
from repositories import booking_repository, gym_class_repository, member_repository

bookings_blueprint = Blueprint("bookings", __name__)


# CREATE
@bookings_blueprint.route("/gym_classes/<id>/add_booking", methods=['POST'])
def create_booking_for_class(id):
    if request.form['add_booking'] == 'None':
        return redirect(request.referrer)
    member_id = request.form['add_booking']
    member = member_repository.select(member_id)
    gym_class = gym_class_repository.select(id)
    booking = Booking(member, gym_class)
    booking_repository.save(booking)
    return redirect(request.referrer)

# CREATE
@bookings_blueprint.route("/members/<id>/add_booking", methods=['POST'])
def create_booking_for_member(id):
    if request.form['add_booking'] == 'None':
        return redirect(request.referrer)
    member = member_repository.select(id)
    gym_class_id = request.form['add_booking']
    gym_class = gym_class_repository.select(gym_class_id)
    booking = Booking(member, gym_class)
    booking_repository.save(booking)
    return redirect(request.referrer)

# DELETE
@bookings_blueprint.route("/gym_classes/<id>/delete_booking", methods=['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect(request.referrer)


