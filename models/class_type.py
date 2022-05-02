from repositories import start_time_repository

class ClassType:
    def __init__(self, title, intensity, description, id=None):
        self.title = title
        self.intensity = intensity
        self.description = description
        self.id = id
    

    def find_available_class_times(self, id):
        available_class_times = []
        all_start_times = start_time_repository.select_all()
        existing_bookings = start_time_repository.select_all_ids_for_class_type(id)
        for time in all_start_times:
            if time.id not in existing_bookings:
                available_class_times.append(time)
        return available_class_times