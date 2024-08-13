from credentials import get_build
from attendance import get_attendance, update_attendance
service = get_build()

attendance_sheet = get_attendance(service)
print(attendance_sheet)

input_value = input("Enter the event name: ")
update_attendance(service, [input_value])
