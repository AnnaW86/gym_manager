all_start_times = ('06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00')

off_peak_times = ('10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00')

peak_times = ('06:00', '07:00', '08:00', '09:00','17:00', '18:00', '19:00', '20:00', '21:00', '22:00')

def check_off_peak_time(time):
    if time in off_peak_times:
        return True

def check_peak_time(time):
    if time in peak_times:
        return True