# Define variables for the premise
students_premise = 14.0
seats_premise = 2.0
buses_premise = students_premise / seats_premise

# Define variables for the hypothesis
buses_hypothesis = 7.0

# Calculate the total number of students that can be transported
total_students_hypothesis = buses_hypothesis * seats_premise

# Check if the total number of students from the hypothesis is greater than or equal to the total number of students in the premise
if total_students_hypothesis >= students_premise:
    # If the total number of students from the hypothesis is greater than or equal to the total number of students in the premise, we can infer entailment
    label = "entailment"
else:
    # If the total number of students from the hypothesis is less than the total number of students in the premise, we can infer contradiction
    label = "contradiction"

print(label)
