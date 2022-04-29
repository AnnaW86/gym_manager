from repositories import gym_class_repository

class GymClass:
    def __init__(self, class_type, start_time, duration, location, capacity, id=None):
        self.class_type = class_type
        self.start_time = start_time
        self.duration = duration
        self.location = location
        self.capacity = capacity
        self.id = id
    
    def get_key_details(self):
        return f"{self.start_time.time } { self.class_type.title }"
    
    def check_availability(self):
        availability = self.capacity - gym_class_repository.check_class_size(self.id)
        return availability

    def check_gym_class_existing_booking(self, member, bookings):
        booked = False
        for booking in bookings:
            if booking.member.id == self.id and booking.gym_class.id == member.id:
                booked = True
                return booked
        return booked
        