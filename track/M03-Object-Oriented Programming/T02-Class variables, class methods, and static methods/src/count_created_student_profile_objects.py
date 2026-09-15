class StudentProfile:
    profile_count = 0

    def __init__(self, name):
        self.name = name
        StudentProfile.profile_count += 1

n = int(input())

for i in range(n):
    name = input().strip()
    StudentProfile(name)

print(f"Profiles Created: {StudentProfile.profile_count}")
