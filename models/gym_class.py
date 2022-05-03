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
    

