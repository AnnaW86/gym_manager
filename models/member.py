from helpers import date_time_helper

class Member:
    def __init__(self, first_name, last_name, membership_number, membership_type, active_status=True, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.membership_number = membership_number
        self.membership_type = membership_type
        self.active_status = active_status
        self.id = id

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def check_existing_booking(self, enrolled_gym_classes, available_classes):
        unbooked_classes = []
        for available_class in available_classes:
            booked = False
            for enrolled_class in enrolled_gym_classes:
                if available_class.id == enrolled_class.id:
                    booked = True
            if booked == False:
                unbooked_classes.append(available_class)
        return unbooked_classes
    
    def find_bookable_classes(self, unbooked_classes):
        bookable_classes = []
        if self.membership_type.title == 'premium':
            return unbooked_classes
        else:
            for unbooked_class in unbooked_classes:
                if unbooked_class.start_time in date_time_helper.off_peak_times:
                    bookable_classes.append(unbooked_class)
            return bookable_classes

    def mark_active_member(self):
        self.active_status = True

    def mark_deactivated_member(self):
        self.active_status = False
    
    def check_premium_member(self):
        if self.membership_type.title == 'premium':
            return True
    
    # def check_bookable_member(self, peak_times, gym_class, members):
    #     bookable_members = []
    #     if date_time_helper.check_off_peak_time(gym_class.time):
    #         bookable_members = members
    #     else:
    #         for member in members:
    #             if self.check_premium_member():
    #                 bookable_members.append(member)
    #     return bookable_members

