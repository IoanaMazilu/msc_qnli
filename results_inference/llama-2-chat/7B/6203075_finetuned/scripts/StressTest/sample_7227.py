# Define the marks Nancy obtained in each subject
literature_marks = 66
history_marks = 75
home_economics_marks = 52
physical_education_marks = 68
art_marks = 89

# Define the marks Nancy obtained in each subject in the hypothesis
hypothesis_literature_marks = 86
hypothesis_history_marks = 75
hypothesis_home_economics_marks = 52
hypothesis_physical_education_marks = 68
hypothesis_art_marks = 89

# Check if the marks in the hypothesis contradict the marks in the premise
if literature_marks > hypothesis_literature_marks:
    label = "contradiction"
elif history_marks > hypothesis_history_marks:
    label = "contradiction"
elif home_economics_marks > hypothesis_home_economics_marks:
    label = "contradiction"
elif physical_education_marks > hypothesis_physical_education_marks:
    label = "contradiction"
elif art_marks > hypothesis_art_marks:
    label = "contradiction"
else:
    label = "neutral"

print(label)
