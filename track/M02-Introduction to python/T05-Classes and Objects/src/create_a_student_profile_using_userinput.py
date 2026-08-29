class StudentProfile:
    def __init__(self,student_id,name,course,score,is_placed):
        self.student_id=student_id
        self.name=name
        self.course=course
        self.score=score
        self.is_placed=is_placed
    def __str__(self):
        placement_status=("Placed" if self.is_placed else "Not Placed")
        return(
            f"{self.student_id} |"
            f"{self.name} |"
            f"{self.course} |"
            f"{self.score:.1f} |"
            f"{placement_status}"
        )

student_id=int(input())
name=input().strip()
course=input().strip()
score=float(input())
placement_input=input().strip()
is_placed=True if placement_input.lower()=="yes" else False
student_one=StudentProfile(student_id,name,course,score,is_placed)
print(student_one)
