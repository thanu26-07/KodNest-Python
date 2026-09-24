class StudentProfile:
    @staticmethod
    def normalize_skill(skill):
        return "_".join(skill.lower().split())

skill_name = input()
normalized = StudentProfile.normalize_skill(skill_name)
print(f"Normalized Skill: {normalized}")
