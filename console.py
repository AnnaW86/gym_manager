from models.member import Member
from models.class_type import ClassType
from models.location import Location
from models.start_time import StartTime

from repositories import member_repository, class_type_repository, location_repository, start_time_repository

member_repository.delete_all()
class_type_repository.delete_all()
location_repository.delete_all()
start_time_repository.delete_all()

member1 = Member("Rachel", "Jones", 123456)
member2 = Member("David", "Bates", 652143)
member3 = Member("Meena", "Zaib", 332753)
member4 = Member("Emilio", "Cortez", 834852)
member5 = Member("Sam", "McDonald", 659536)
member6 = Member("Charlie", "Davies", 748593)
member7 = Member("Susan", "Stevens", 345379)
member8 = Member("Petra", "Parrot", 365495)
member9 = Member("Guillaume", "Barca", 568752)
member10 = Member("Sacha", "Cortz", 193946)
member11 = Member("Russel", "Wentsworth", 887456)
member12 = Member("David", "MacLaren", 876924)
member13 = Member("Ahmad", "Baqri", 531123)
member14 = Member("Emily", "Robinson", 848435)
member15 = Member("Kit", "Bilson", 384200)

members = [member1,member2,member3,member4,member5,member6,member7,member8,member9,member10,member11,member12,member13,member14,member15]

for member in members:
    member_repository.save(member)


spin = ClassType('Spin', 4, 'Hard work')
class_type_repository.save(spin)
pilates = ClassType('Pilates', 2, 'Tone and strengthen')
class_type_repository.save(pilates)
hiit = ClassType('HIIT', 5, 'High impact')
class_type_repository.save(hiit)
aquafit = ClassType('Aquafit', 2, 'Low impact strengthening')
class_type_repository.save(aquafit)

location1 = Location('Main gym')
location_repository.save(location1)
location2 = Location('Studio')
location_repository.save(location2)
location3 = Location('Pool')
location_repository.save(location3)

am6 = StartTime('6am')
am7 = StartTime('7am')
am8 = StartTime('8am')
am9 = StartTime('9am')
am10 = StartTime('10am')
am11 = StartTime('11am')
pm12 = StartTime('12pm')
pm1 = StartTime('1pm')
pm2 = StartTime('2pm')
pm3 = StartTime('3pm')
pm4 = StartTime('4pm')
pm5 = StartTime('5pm')
pm6 = StartTime('6pm')
pm7 = StartTime('7pm')
pm8 = StartTime('8pm')
pm9 = StartTime('9pm')
pm10 = StartTime('10pm')

start_times = [am6,am7,am8,am9,am10,am11,pm12,pm1,pm2,pm3,pm4,pm5,pm6,pm7,pm8,pm9,pm10]

for time in start_times:
    start_time_repository.save(time)