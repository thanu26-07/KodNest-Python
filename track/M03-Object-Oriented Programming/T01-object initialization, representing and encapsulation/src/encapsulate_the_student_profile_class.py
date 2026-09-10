class StudentProfile:
    def __init__(self, student_id, name, score, skills):
        self.__student_id = student_id
        self.__name = name
        self.__score = score
        self.__skills = list(skills)

    @property
    def student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name.strip() != "":
            self.__name = new_name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        if 0 <= new_score <= 100:
            self.__score = new_score

    @property
    def skills(self):
        return tuple(self.__skills)

    def add_skill(self, new_skill):
        cleaned_skill = new_skill.strip()
        if cleaned_skill and cleaned_skill not in self.__skills:
            self.__skills.append(cleaned_skill)

    def __str__(self):
        skills_text = ", ".join(self.__skills)
        return (
            f"STUDENT PROFILE\n"
            f"Student ID: {self.__student_id}\n"
            f"Name: {self.__name}\n"
            f"Score: {self.__score}\n"
            f"Skills: {skills_text}"
        )


student_id = int(input())
name = input().strip()
initial_score = int(input())
skills_input = input().strip()
new_score = int(input())
new_skill = input().strip()

initial_skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]

student = StudentProfile(student_id, name, initial_score, initial_skills)
student.score = new_score
student.add_skill(new_skill)

print(student)
