# Calculate the average marks of a student
# in the given subjects

# Define the marks obtained by the student
marks = [56, 60, 72, 85, 80]

# Calculate the average marks
average_marks = sum(marks) / len(marks)

# Define the hypothesis
hypothesis_marks = [26, 60, 72, 85, 80]

# Check if the hypothesis contradicts the premise
if average_marks <= hypothesis_marks:
    label = "contradiction"
else:
    label = "neutral"

print(label)
