class StudentProfile:
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if 0 <= new_score <= 100:
            self.__score = new_score
            return True
        else:
            return False


name = input().strip()
initial_score = int(input())
new_score = int(input())

student = StudentProfile(name, initial_score)
bool_res = student.set_score(new_score)

if bool_res:
    print("Score Updated")
else:
    print("Invalid Score")

print(f"Name: {student.name}")
print(f"Final Score: {student.get_score()}")
