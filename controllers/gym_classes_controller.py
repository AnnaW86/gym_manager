from flask import Blueprint, render_template, redirect, request

from models.gym_class import GymClass
from repositories import gym_class_repository

gym_classes_blueprint = Blueprint("gym_classes", __name__)

#INDEX
@gym_classes_blueprint.route("/gym_classes")
def classes():
    return render_template("gym_classes/index.html", gym_classes = gym_class_repository.select_all())