from flask import Blueprint, render_template, request, redirect

from models.booking import Booking
from repositories import booking_repository, gym_class_repository, member_repository

bookings_blueprint = Blueprint("bookings", __name__)


# CREATE
@bookings_blueprint.route("/gym_classes/<id>/add_booking", methods=['POST'])
def create_booking(id):
    member_id = request.form['add_booking']
    member = member_repository.select(member_id)
    gym_class = gym_class_repository.select(id)
    booking = Booking(member, gym_class)
    booking_repository.save(booking)
    return redirect(request.referrer)

# DELETE
@bookings_blueprint.route("/gym_classes/<id>/delete_booking", methods=['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect(request.referrer)


