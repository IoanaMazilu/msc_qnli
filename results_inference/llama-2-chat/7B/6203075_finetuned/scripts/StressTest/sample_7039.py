# Define variables for the marks obtained by the student in each subject
geography_marks = 26
history_marks = 60
government_marks = 72
art_marks = 85
literature_marks = 80

# Define the marks obtained by the student in the hypothesis
hypothesis_geography_marks = 56
hypothesis_history_marks = 60
hypothesis_government_marks = 72
hypothesis_art_marks = 85
hypothesis_literature_marks = 80

# Calculate the average marks of the student in each subject in the premise
average_geography_marks = (geography_marks + history_marks + government_marks + art_marks + literature_marks) / 5
average_history_marks = (history_marks + government_marks + art_marks + literature_marks) / 4
average_government_marks = (government_marks + art_marks + literature_marks) / 3
average_art_marks = (art_marks + literature_marks) / 2
average_literature_marks = literature_marks

# Calculate the average marks of the student in each subject in the hypothesis
average_geography_marks_hypothesis = (hypothesis_geography_marks + history_marks + government_marks + art_marks + literature_marks) / 5
average_history_marks_hypothesis = (history_marks + government_marks + art_marks + literature_marks) / 4
average_government_marks_hypothesis = (government_marks + art_marks + literature_marks) / 3
average_art_marks_hypothesis = (art_marks + literature_marks) / 2
average_literature_marks_hypothesis = literature_marks

# Check if the average marks in each subject in the hypothesis contradicts or is consistent with the average marks in each subject in the premise
if average_geography_marks_hypothesis!= average_geography_marks:
    label = "contradiction"
elif average_history_marks_hypothesis!= average_history_marks:
    label = "contradiction"
elif average_government_marks_hypothesis!= average_government_marks:
    label = "contradiction"
elif average_art_marks_hypothesis!= average_art_marks:
    label = "contradiction"
elif average_literature_marks_hypothesis!= average_literature_marks:
    label = "contradiction"
else:
    label = "neutral"

print(label)
