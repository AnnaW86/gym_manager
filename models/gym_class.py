from repositories import gym_class_repository
from helpers import date_time_helper
from models.member import Member


class GymClass:
    def __init__(self, class_type, start_time, duration, location, capacity, id=None):
        self.class_type = class_type
        self.start_time = start_time
        self.duration = duration
        self.location = location
        self.capacity = capacity
        self.id = id
    
    def get_key_details(self):
        return f"{self.start_time } { self.class_type.title }"
    
    def check_availability(self):
        availability = self.capacity - gym_class_repository.number_of_bookings(self.id)
        return availability
    
    def check_members_existing_booking(self, members, enrolled_members):
        unbooked_members = []
        for member in members:
            booked = False
            for enrolled_member in enrolled_members:
                if member.id == enrolled_member.id:
                    booked = True
            if booked == False:
                unbooked_members.append(member)
        return unbooked_members
        
    def find_bookable_members(self, members):
        bookable_members = []
        if date_time_helper.check_off_peak_time(self.start_time):
            return members
        else:
            for member in members:
                if member.check_premium_member():
                    bookable_members.append(member)
            return bookable_members

