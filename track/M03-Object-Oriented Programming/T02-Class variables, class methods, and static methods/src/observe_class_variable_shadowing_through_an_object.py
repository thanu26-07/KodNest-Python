class TrainingBatch:
    batch_name = "Python Batch 1"

    def __init__(self, student_name):
        self.student_name = student_name

student1_name = input().strip()
student2_name = input().strip()
special_batch = input().strip()
new_shared_batch = input().strip()

training1 = TrainingBatch(student1_name)
training2 = TrainingBatch(student2_name)

training1.batch_name = special_batch
TrainingBatch.batch_name = new_shared_batch

print(f"Class Batch: {TrainingBatch.batch_name}")
print(f"{student1_name} Batch: {training1.batch_name}")
print(f"{student2_name} Batch: {training2.batch_name}")
