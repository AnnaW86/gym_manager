from flask import Blueprint, render_template, request, redirect

from models.class_type import ClassType
from repositories import class_type_repository

class_types_blueprint = Blueprint("class_types", __name__)

# INDEX
@class_types_blueprint.route("/class_types")
def class_types():
    return render_template("class_types/index.html", class_types = class_type_repository.select_all())

# NEW
@class_types_blueprint.route("/class_types/new")
def new_class_type():
    return render_template("class_types/new.html")

# CREATE
@class_types_blueprint.route("/class_types", methods=['POST'])
def create_class_type():
    title = request.form['title']
    intensity = request.form['intensity']
    description = request.form['description']
    class_type = ClassType(title, intensity, description)
    class_type_repository.save(class_type)
    return redirect('/class_types')