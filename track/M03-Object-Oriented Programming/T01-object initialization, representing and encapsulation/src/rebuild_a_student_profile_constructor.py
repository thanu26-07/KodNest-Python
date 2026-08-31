class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        course,
        experience,
        skills
    ):
        # Store all received values as instance attributes
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills

# Read inputs from the user
student_id = int(input().strip())
name = input().strip()
course = input().strip()
experience = int(input().strip())
skills = input().split()

# Create one StudentProfile object
student1 = StudentProfile(student_id, name, course, experience, skills)

# Print the data stored in the object
print(f"Student ID: {student1.student_id}\nName: {student1.name}\nCourse: {student1.course}\nExperience in Years: {student1.experience}\nSkills: {', '.join(student1.skills)}")
