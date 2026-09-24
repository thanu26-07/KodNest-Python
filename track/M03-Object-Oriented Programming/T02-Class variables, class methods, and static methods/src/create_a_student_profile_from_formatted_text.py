class StudentProfile:
    def __init__(self, student_id, name, course, experience):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience

    @classmethod
    def from_text(cls, data):
        student_id, name, course, experience = data.split("|")
        return cls(student_id, name, course, int(experience))

data = input().strip()
student = StudentProfile.from_text(data)

print(f"Student ID: {student.student_id}\nName: {student.name}\nCourse: {student.course}\nExperience: {student.experience} years")
