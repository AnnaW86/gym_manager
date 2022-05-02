from flask import Blueprint, render_template, redirect, request

from models.gym_class import GymClass
from models.class_type import ClassType
from repositories import gym_class_repository, member_repository, class_type_repository, location_repository
from helpers import date_time_helper

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
    start_times = class_type.find_available_class_times(id)
    locations = location_repository.select_all()
    return render_template("gym_classes/new.html", class_type = class_type, class_types = class_types, start_times = start_times, locations = locations)

# CREATE
@gym_classes_blueprint.route("/gym_classes/class_type/<id>", methods = ['POST'])
def create_class(id):
    class_type = gym_class_repository.select(id).class_type
    start_time = request.form['start_time']
    duration = request.form['duration']
    location_id = request.form['location']
    location = location_repository.select(location_id)
    capacity = request.form['capacity']
    gym_class = GymClass(class_type, start_time, duration, location, capacity)
    gym_class_repository.save(gym_class)
    return redirect(f"/class_types/{class_type.id}")

# # UPDATE
# @gym_classes_blueprint.route("/gym_classes/<id>", methods=['POST'])
# def update_gym_class(id):
    # breakpoint()


    


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


# EDIT
@gym_classes_blueprint.route("/gym_classes/<id>/edit")
def edit_gym_class(id):
    gym_class = gym_class_repository.select(id)
    start_times = gym_class.class_type.find_available_class_times(gym_class.class_type.id)
    start_times.insert(0, gym_class.start_time)
    locations = location_repository.select_all()
    return render_template("gym_classes/edit.html", gym_class = gym_class, start_times = start_times, locations = locations, class_types = class_type_repository.select_all())

# UPDATE
@gym_classes_blueprint.route("/gym_classes/<id>", methods=['POST'])
def update_gym_class(id):
    gym_class = gym_class_repository.select(id)
    start_time = request.form['start_time']
    location_id = request.form['location']
    location = location_repository.select(location_id)
    gym_class = GymClass(gym_class.class_type, start_time, gym_class.duration, location, gym_class.capacity, id)
    gym_class_repository.update(gym_class)
    return redirect(f"/gym_classes/{id}")