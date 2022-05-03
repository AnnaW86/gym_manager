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

    def mark_active_member(self):
        self.active_status = True

    def mark_deactivated_member(self):
        self.active_status = False
    
    def check_premium_member(self):
        if self.membership_type.title == 'premium':
            return True
    

