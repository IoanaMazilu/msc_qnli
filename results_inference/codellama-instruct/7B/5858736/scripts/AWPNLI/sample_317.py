# Define variables for the premise
num_students_premise = 390.0
num_students_per_classroom_premise = 30.0

# Define variables for the hypothesis
num_classrooms_hypothesis = 11.0

# Calculate the total number of students in each classroom
num_students_per_classroom_hypothesis = num_students_premise / num_classrooms_hypothesis

# Check if the number of students in each classroom from the hypothesis contradicts the estimate from the premise
if num_students_per_classroom_hypothesis!= num_students_per_classroom_premise:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
