# defining the marks obtained by the student in each subject according to the premise
geography_marks_premise = 56
history_marks_premise = 60
government_marks_premise = 72
art_marks_premise = 85
computer_science_marks_premise = 80

# defining the marks obtained by the student in each subject according to the hypothesis
geography_marks_hypothesis = 56
history_marks_hypothesis = 60
government_marks_hypothesis = 72
art_marks_hypothesis = 85
computer_science_marks_hypothesis = 80

# the hypothesis refers to the marks obtained by the student in each subject mentioned in the premise
if geography_marks_hypothesis >= geography_marks_premise or history_marks_hypothesis >= history_marks_premise or government_marks_hypothesis >= government_marks_premise or art_marks_hypothesis >= art_marks_premise or computer_science_marks_hypothesis >= computer_science_marks_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
