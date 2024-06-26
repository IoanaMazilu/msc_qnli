math_marks_premise = 46
math_marks_hypothesis = 76
science_marks_premise = 65
science_marks_hypothesis = 65
social_studies_marks_premise = 82
social_studies_marks_hypothesis = 82
english_marks_premise = 67
english_marks_hypothesis = 67
biology_marks_premise = 75
biology_marks_hypothesis = 75

# the hypothesis refers to the marks scored by Shekar in different subjects mentioned in the premise
if math_marks_hypothesis <= math_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than'math_marks_premise'
    label = "contradiction"
elif science_marks_hypothesis!= science_marks_premise or social_studies_marks_hypothesis!= social_studies_marks_premise or english_marks_hypothesis!= english_marks_premise or biology_marks_hypothesis!= biology_marks_premise:
    # check if the marks in any of the subjects in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks in Mathematics
    # any marks greater than'math_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
