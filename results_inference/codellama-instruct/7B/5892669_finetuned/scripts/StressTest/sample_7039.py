geography_marks_premise = 26
history_marks_premise = 60
government_marks_premise = 72
art_marks_premise = 85
computer_science_marks_premise = 80

geography_marks_hypothesis = 56
history_marks_hypothesis = 60
government_marks_hypothesis = 72
art_marks_hypothesis = 85
computer_science_marks_hypothesis = 80

# the hypothesis refers to the marks obtained by a student in different subjects, mentioned in the premise
if geography_marks_hypothesis <= geography_marks_premise or history_marks_hypothesis!= history_marks_premise or government_marks_hypothesis!= government_marks_premise or art_marks_hypothesis!= art_marks_premise or computer_science_marks_hypothesis!= computer_science_marks_premise:
    # check if the marks obtained in the hypothesis contradict the marks obtained in the premise
    label = "contradiction"
elif geography_marks_hypothesis > geography_marks_premise:
    # check if the estimate of 'geography_marks_hypothesis' contradicts the number of geography marks in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of geography marks
    # any number of geography marks greater than 'geography_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
