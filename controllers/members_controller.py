from flask import Blueprint, render_template, request, redirect

from models.member import Member
from repositories import member_repository, gym_class_repository, class_type_repository, membership_type_repository, booking_repository

members_blueprint = Blueprint("members", __name__)

# INDEX
@members_blueprint.route("/members", methods=['GET'])
def members():
    active_members = member_repository.select_all_active()
    deactivated_members = member_repository.select_all_by_deactivated()
    membership_types = membership_type_repository.select_all()
    return render_template("members/index.html", active_members = active_members, deactivated_members = deactivated_members, membership_types = membership_types, class_types = class_type_repository.select_all())

# NEW
@members_blueprint.route("/members/new")
def new_member():
    members = member_repository.select_all()
    membership_types = membership_type_repository.select_all()
    return render_template("members/new.html", members = members, membership_types = membership_types, class_types = class_type_repository.select_all())

# CREATE
@members_blueprint.route("/members", methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    membership_number = request.form['membership_number']
    membership_type_id = request.form['membership_type']
    membership_type = membership_type_repository.select(membership_type_id)
    member = Member(first_name, last_name, membership_number, membership_type)
    member_repository.save(member)
    return redirect('/members')

# SHOW
@members_blueprint.route("/members/<id>")
def show_member(id):
    member = member_repository.select(id)
    enrolled_gym_classes = gym_class_repository.select_all_by_enrolled_member(id)
    available_classes = gym_class_repository.find_available_classes()
    available_places = member_repository.find_available_places(id)
    unbooked_classes = gym_class_repository.find_unbooked_classes(enrolled_gym_classes, available_classes)
    bookable_classes = gym_class_repository.find_bookable_classes(member, unbooked_classes)
    return render_template("members/show.html", member = member, enrolled_gym_classes = enrolled_gym_classes, bookable_classes = bookable_classes, available_places = available_places, class_types = class_type_repository.select_all())

# EDIT
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("members/edit.html", member = member, class_types = class_type_repository.select_all())

# UPDATE
@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    member = member_repository.select(id)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    membership_number = request.form['membership_number']
    membership_type_title = request.form['membership_type']
    membership_type = membership_type_repository.select_from_type(membership_type_title)
    active_status_feedback = request.form['account_status']
    if active_status_feedback == 'deactivated':
        member.mark_deactivated_member()
        booking_repository.delete_all_by_member_id(id)
    if active_status_feedback == 'active':
        member.mark_active_member()
    member = Member(first_name, last_name, membership_number, membership_type, member.active_status, id)
    member_repository.update(member)
    return redirect(f"/members/{id}")