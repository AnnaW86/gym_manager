from flask import Blueprint, render_template, redirect, request

from models.gym_class import GymClass
from repositories import gym_class_repository, member_repository, start_time_repository, class_type_repository, location_repository

gym_classes_blueprint = Blueprint("gym_classes", __name__)

# INDEX
@gym_classes_blueprint.route("/gym_classes")
def classes():
    class_types = class_type_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/index.html", class_types = class_types, gym_classes = gym_classes)

# NEW
@gym_classes_blueprint.route("/class_types/<id>/new_session")
def new_class(id):
    class_type = class_type_repository.select(id)
    class_types = class_type_repository.select_all()
    start_times = start_time_repository.select_all()
    locations = location_repository.select_all()
    return render_template("gym_classes/new.html", class_type = class_type, class_types = class_types, start_times = start_times, locations = locations)

# CREATE
@gym_classes_blueprint.route("/gym_classes/<id>", methods = ['POST'])
def create_class(id):
    class_type = class_type_repository.select(id)
    start_time_id = request.form['start_time']
    start_time = start_time_repository.select(start_time_id)
    duration = request.form['duration']
    location_id = request.form['location']
    location = location_repository.select(location_id)
    capacity = request.form['capacity']
    gym_class = GymClass(class_type, start_time, duration, location, capacity)
    gym_class_repository.save(gym_class)
    return redirect(f"/class_types/{id}")


# SHOW
@gym_classes_blueprint.route("/gym_classes/<id>")
def show_gym_class(id):
    gym_class = gym_class_repository.select(id)
    number_of_attendees = member_repository.find_number_of_attendees(id)
    attendees = member_repository.select_all_by_gym_class(id)
    availability = gym_class.check_availability()
    members =  member_repository.select_all_active()
    unbooked_members = []
    enrolled_members = member_repository.select_all_by_gym_class(id)
    gym_class.check_members_existing_booking(members, enrolled_members, unbooked_members)
    return render_template("gym_classes/show.html", gym_class = gym_class, number_of_attendees = number_of_attendees, attendees = attendees, availability = availability, unbooked_members = unbooked_members, class_types = class_type_repository.select_all() )
