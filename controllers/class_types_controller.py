from flask import Blueprint, render_template, request, redirect

from models.class_type import ClassType
from repositories import class_type_repository, gym_class_repository

class_types_blueprint = Blueprint("class_types", __name__)

# INDEX
@class_types_blueprint.route("/class_types")
def class_types():
    return render_template("class_types/index.html", class_types = class_type_repository.select_all())

# NEW
@class_types_blueprint.route("/class_types/new")
def new_class_type():
    return render_template("class_types/new.html", class_types = class_type_repository.select_all())

# CREATE
@class_types_blueprint.route("/class_types", methods=['POST'])
def create_class_type():
    title = request.form['title']
    intensity = request.form['intensity']
    description = request.form['description']
    class_type = ClassType(title, intensity, description)
    class_type_repository.save(class_type)
    return redirect('/class_types')

# SHOW
@class_types_blueprint.route("/class_types/<id>")
def show_class_type(id):
    class_type = class_type_repository.select(id)
    filtered_classes = gym_class_repository.select_by_class_type_id(id)
    number_of_scheduled_classes = gym_class_repository.find_number_of_classes_scheduled(id)
    return render_template("class_types/show.html", class_type = class_type, filtered_classes = filtered_classes, number_of_scheduled_classes = number_of_scheduled_classes, class_types = class_type_repository.select_all())

# EDIT
@class_types_blueprint.route("/class_types/<id>/edit")
def edit_class_type(id):
    class_type = class_type_repository.select(id)
    return render_template("class_types/edit.html", class_type = class_type, class_types = class_type_repository.select_all())

# UPDATE
@class_types_blueprint.route("/class_types/<id>", methods=['POST'])
def update_class_type(id):
    title = request.form['title']
    intensity = request.form['intensity']
    description = request.form['description']
    class_type = ClassType(title, intensity, description, id)
    class_type_repository.update(class_type)
    return redirect(f"/class_types/{id}")
