geography_marks_premise = 56
history_marks_premise = 60
government_marks_premise = 72
art_marks_premise = 85
computer_science_marks_premise = 80

geography_marks_hypothesis = 26
history_marks_hypothesis = 60
government_marks_hypothesis = 72
art_marks_hypothesis = 85
computer_science_marks_hypothesis = 80

# the hypothesis refers to the marks obtained by a student in various subjects mentioned in the premise
if geography_marks_premise <= geography_marks_hypothesis or history_marks_premise!= history_marks_hypothesis or government_marks_premise!= government_marks_hypothesis or art_marks_premise!= art_marks_hypothesis or computer_science_marks_premise!= computer_science_marks_hypothesis:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
