from flask import Blueprint, render_template, redirect, request

from models.gym_class import GymClass
from repositories import gym_class_repository, member_repository

gym_classes_blueprint = Blueprint("gym_classes", __name__)

# INDEX
@gym_classes_blueprint.route("/gym_classes")
def classes():
    return render_template("gym_classes/index.html", gym_classes = gym_class_repository.select_all())


# SHOW
@gym_classes_blueprint.route("/gym_classes/<id>")
def show_gym_class(id):
    gym_class = gym_class_repository.select(id)
    attendees = member_repository.select_all_by_gym_class(gym_class)
    members =  member_repository.select_all()
    return render_template("gym_classes/show.html", gym_class = gym_class, attendees = attendees, members = members )
