class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"

class PlacementManager:
    def __init__(self):
        self.student_profiles = []

    def add_student_profile(self, student_profile):
        self.student_profiles.append(student_profile)

    def filter_students_by_course(self, search):
        found = False
        for profile in self.student_profiles:
            if profile.course.lower() == search.lower():
                found = True
                print(profile)
        if not found:
            print(f"No students found for course: {search}")

manager = PlacementManager()
n = int(input())

for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()
    student = StudentProfile(student_id, name, course)
    manager.add_student_profile(student)

search = input().strip()
manager.filter_students_by_course(search)
