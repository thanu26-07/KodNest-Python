class TrainingBatch:
    batch_name = "Python Batch 1"
    
    def __init__(self, student_name):
        self.student_name = student_name
        
    @classmethod
    def update_batch_name(cls, new_batch_name):
        cls.batch_name = new_batch_name

student1_name = input().strip()
student2_name = input().strip()
new_batch_name = input().strip()

stu1 = TrainingBatch(student1_name)
stu2 = TrainingBatch(student2_name)

TrainingBatch.update_batch_name(new_batch_name)

print("Updated Batch:", TrainingBatch.batch_name)
print(f"{stu1.student_name}: {stu1.batch_name}")
print(f"{stu2.student_name}: {stu2.batch_name}")
