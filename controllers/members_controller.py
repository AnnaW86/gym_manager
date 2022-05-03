from zoneinfo import available_timezones
from flask import Blueprint, render_template, request, redirect

from models.member import Member
from repositories import member_repository, gym_class_repository, class_type_repository, membership_type_repository, booking_repository

members_blueprint = Blueprint("members", __name__)

# INDEX
@members_blueprint.route("/members")
def members():
    active_members = member_repository.select_all_active()
    deactivated_members = member_repository.select_all_by_deactivated()
    return render_template("members/index.html", active_members = active_members, deactivated_members = deactivated_members, class_types = class_type_repository.select_all())

# NEW
@members_blueprint.route("/members/new")
def new_member():
    members = member_repository.select_all()
    return render_template("members/new.html", members = members, class_types = class_type_repository.select_all())

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
    available_classes = []
    for gym_class in all_gym_classes:
        if gym_class.check_availability() > 0:
            available_classes.append(gym_class)
    
    number_of_bookings = member_repository.find_number_of_bookings(id)
    unbooked_classes = member.check_existing_booking(enrolled_gym_classes, available_classes)
    bookable_classes = member.find_bookable_classes(unbooked_classes)
    return render_template("members/show.html", member = member, enrolled_gym_classes = enrolled_gym_classes, bookable_classes = bookable_classes, number_of_bookings = number_of_bookings, class_types = class_type_repository.select_all())

# EDIT
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("members/edit.html", member = member, class_types = class_type_repository.select_all())

# UPDATE
@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    membership_number = request.form['membership_number']
    membership_type_title = request.form['membership_type']
    membership_type = membership_type_repository.select_from_type(membership_type_title)
    active_status_feedback = request.form['account_status']
    if active_status_feedback == 'deactivated':
        active_status = False
        booking_repository.delete_all_by_member_id(id)
    if active_status_feedback == 'active':
        active_status = True
    member = Member(first_name, last_name, membership_number, membership_type, active_status, id)
    member_repository.update(member)
    return redirect(f"/members/{id}")
