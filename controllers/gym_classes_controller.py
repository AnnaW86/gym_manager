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
    unbooked_members = []
    enrolled_members = member_repository.select_all_by_gym_class(id)
    for member in members:
        booked = False
        for enrolled_member in enrolled_members:
            if member.id == enrolled_member.id:
                booked = True
        if booked == False:
            unbooked_members.append(member)
    return render_template("gym_classes/show.html", gym_class = gym_class, attendees = attendees, availability = availability, unbooked_members = unbooked_members )
