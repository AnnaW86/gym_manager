from flask import Blueprint, render_template, request, redirect

from models.member import Member
from repositories import member_repository, gym_class_repository

members_blueprint = Blueprint("members", __name__)

# INDEX
@members_blueprint.route("/members")
def members():
    return render_template("members/index.html", members = member_repository.select_all())

# NEW
@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/new.html", )

# CREATE
@members_blueprint.route("/members", methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    membership_number = request.form['membership_number']
    member = Member(first_name, last_name, membership_number)
    member_repository.save(member)
    return redirect('/members')

# SHOW
@members_blueprint.route("/members/<id>")
def show_member(id):
    member = member_repository.select(id)
    enrolled_gym_classes = gym_class_repository.select_all_by_enrolled_member(id)
    all_gym_classes = gym_class_repository.select_all()
    return render_template("members/show.html", member = member, enrolled_gym_classes = enrolled_gym_classes, all_gym_classes = all_gym_classes)

# EDIT
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("members/edit.html", member = member)

# UPDATE
@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    membership_number = request.form['membership_number']
    member = Member(first_name, last_name, membership_number, id)
    member_repository.update(member)
    return render_template("members/show.html", member = member)

# CLASS USERS' SHOW
# @members_blueprint.route("/gym_classes/<id>")
