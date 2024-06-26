# Define variables for the marks obtained by the student in each subject
geography_mark = 56
history_mark = 60
government_mark = 72
art_mark = 85
computer_science_mark = 80
modern_literature_mark = 80

# Calculate the average marks of the student
average_marks = (geography_mark + history_mark + government_mark + art_mark + computer_science_mark + modern_literature_mark) / 6

# Check if the hypothesis is entailed from the premise
if average_marks > 26:
    label = "entailment"
else:
    label = "contradiction"

print(label)
