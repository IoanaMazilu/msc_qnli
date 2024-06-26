geography_marks_premise = 26
geography_marks_hypothesis = 56
history_marks_premise = 60
history_marks_hypothesis = 60
government_marks_premise = 72
government_marks_hypothesis = 72
art_marks_premise = 85
art_marks_hypothesis = 85
computer_science_marks_premise = 80
computer_science_marks_hypothesis = 80
modern_literature_marks_premise = 80
modern_literature_marks_hypothesis = 80

# the hypothesis refers to the marks obtained by a student in various subjects mentioned in the premise
if geography_marks_hypothesis <= geography_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'geography_marks_premise'
    label = "contradiction"
elif history_marks_hypothesis!= history_marks_premise or government_marks_hypothesis!= government_marks_premise or art_marks_hypothesis!= art_marks_premise or computer_science_marks_hypothesis!= computer_science_marks_premise or modern_literature_marks_hypothesis!= modern_literature_marks_premise:
    # check if the marks in any of the subjects in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks in Geography
    # any marks greater than 'geography_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
