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

# the hypothesis refers to the marks scored by Shekar in different subjects mentioned in the premise
if math_marks_hypothesis <= math_marks_premise or science_marks_hypothesis <= science_marks_premise or social_studies_marks_hypothesis <= social_studies_marks_premise or english_marks_hypothesis <= english_marks_premise or biology_marks_hypothesis <= biology_marks_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
