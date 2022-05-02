from repositories import gym_class_repository, start_time_repository

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
    
    def check_members_existing_booking(self, members, enrolled_members, unbooked_members):
        for member in members:
            booked = False
            for enrolled_member in enrolled_members:
                if member.id == enrolled_member.id:
                    booked = True
            if booked == False:
                unbooked_members.append(member)
        return unbooked_members
    
    def find_available_sessions(self, gym_classes, booked_start_times_ids):
        available_sessions = []
        for gym_class in gym_classes:
            if gym_class.start_time.id not in booked_start_times_ids:
                start_time = start_time_repository.select(gym_class.start_time.id)
                available_sessions.append(start_time)
        return available_sessions
