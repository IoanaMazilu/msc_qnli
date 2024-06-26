# defining the marks obtained by the student in each subject according to the premise
geography_marks_premise = 56
history_marks_premise = 60
government_marks_premise = 72
art_marks_premise = 85
computer_science_marks_premise = 80

# defining the marks obtained by the student in each subject according to the hypothesis
geography_marks_hypothesis = 26
history_marks_hypothesis = 60
government_marks_hypothesis = 72
art_marks_hypothesis = 85
computer_science_marks_hypothesis = 80

# the hypothesis refers to the marks obtained by the student in each subject mentioned in the premise
if geography_marks_hypothesis > geography_marks_premise:
    # check if the estimate of 'geography_marks_hypothesis' contradicts the number of geography marks in the premise
    label = "contradiction"
elif history_marks_hypothesis!= history_marks_premise or government_marks_hypothesis!= government_marks_premise or art_marks_hypothesis!= art_marks_premise or computer_science_marks_hypothesis!= computer_science_marks_premise:
    # check if the number of marks in any of the other subjects in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)