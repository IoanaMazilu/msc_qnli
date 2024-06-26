# defining the marks scored by Adam in the premise
french_marks_premise = 86
geography_marks_premise = 75
art_marks_premise = 72
history_marks_premise = 63
physical_education_marks_premise = 65

# defining the marks scored by Adam in the hypothesis
french_marks_hypothesis = 86
geography_marks_hypothesis = 75
art_marks_hypothesis = 72
history_marks_hypothesis = 63
physical_education_marks_hypothesis = 65

# the hypothesis refers to the marks scored by Adam in the premise
if french_marks_hypothesis <= french_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'french_marks_premise'
    label = "contradiction"
elif geography_marks_hypothesis!= geography_marks_premise or art_marks_hypothesis!= art_marks_premise or history_marks_hypothesis!= history_marks_premise or physical_education_marks_hypothesis!= physical_education_marks_premise:
    # check if the marks in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the French marks
    # any number of French marks greater than 'french_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
