# Premise: Nancy obtained less than 86, 75, 52, 68 and 89 marks (out of 100) in American Literature, History, Home Economics, Physical Education and Art.
# Hypothesis: Nancy obtained 66, 75, 52, 68 and 89 marks (out of 100) in American Literature, History, Home Economics, Physical Education and Art.
# Golden Label: neutral

lit_marks_premise = 86
hist_marks_premise = 75
home_eco_marks_premise = 52
pe_marks_premise = 68
art_marks_premise = 89

lit_marks_hypothesis = 66
hist_marks_hypothesis = 75
home_eco_marks_hypothesis = 52
pe_marks_hypothesis = 68
art_marks_hypothesis = 89

# the hypothesis talks about the marks obtained by Nancy in different subjects, also mentioned in the premise
if lit_marks_hypothesis >= lit_marks_premise or hist_marks_hypothesis > hist_marks_premise or home_eco_marks_hypothesis > home_eco_marks_premise or pe_marks_hypothesis > pe_marks_premise or art_marks_hypothesis > art_marks_premise:
    # check if the hypothesis values contradict the estimates of less than 'subject_marks_premise'
    label = "contradiction"
elif lit_marks_hypothesis < lit_marks_premise and hist_marks_hypothesis == hist_marks_premise and home_eco_marks_hypothesis == home_eco_marks_premise and pe_marks_hypothesis == pe_marks_premise and art_marks_hypothesis == art_marks_premise:
    # check if the hypothesis values are the same or less than the premise values
    label = "entailment"
else:
    # the premise gives only an estimate for the number of marks
    # any number of marks less than 'subject_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

