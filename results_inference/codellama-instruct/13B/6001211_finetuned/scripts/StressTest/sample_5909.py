math_marks_premise = 76
science_marks_premise = 65
social_studies_marks_premise = 82
english_marks_premise = 67
biology_marks_premise = 75

math_marks_hypothesis = 76
science_marks_hypothesis = 65
social_studies_marks_hypothesis = 82
english_marks_hypothesis = 67
biology_marks_hypothesis = 75

# the hypothesis refers to the marks scored by Shekar in various subjects mentioned in the premise
if math_marks_hypothesis <= math_marks_premise or science_marks_hypothesis <= science_marks_premise or social_studies_marks_hypothesis <= social_studies_marks_premise or english_marks_hypothesis <= english_marks_premise or biology_marks_hypothesis <= biology_marks_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives exact marks for each subject
    # any marks greater than the premise ones is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
