from zoneinfo import available_timezones
from flask import Blueprint, render_template, redirect, request

from models.gym_class import GymClass
from repositories import gym_class_repository, member_repository, start_time_repository, class_type_repository, booking_repository

gym_classes_blueprint = Blueprint("gym_classes", __name__)

# INDEX
@gym_classes_blueprint.route("/gym_classes")
def classes():
    class_types = class_type_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/index.html", class_types = class_types, gym_classes = gym_classes)


# SHOW
@gym_classes_blueprint.route("/gym_classes/<id>")
def show_gym_class(id):
    gym_class = gym_class_repository.select(id)
    attendees = member_repository.select_all_by_gym_class(id)
    availability = gym_class.check_availability()
    members =  member_repository.select_all()
    bookings = booking_repository.select_all()
    unbooked_members = []
    for member in members:
        if gym_class.check_gym_class_existing_booking(member, bookings) == False:
            unbooked_members.append(member)
    breakpoint()
    return render_template("gym_classes/show.html", gym_class = gym_class, attendees = attendees, availability = availability, unbooked_members = unbooked_members )
