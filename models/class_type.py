from repositories import class_type_repository
from helpers import date_time_helper

class ClassType:
    def __init__(self, title, intensity, description, id=None):
        self.title = title
        self.intensity = intensity
        self.description = description
        self.id = id
    

    def find_available_class_times(self, id):
        available_class_times = []
        all_start_times = date_time_helper.all_start_times
        existing_bookings = class_type_repository.select_all_booked_times(id)
        for time in all_start_times:
            if time not in existing_bookings:
                available_class_times.append(time)
        return available_class_times
    