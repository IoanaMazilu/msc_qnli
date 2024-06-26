math_marks_premise = 76
science_marks_premise = 65
social_studies_marks_premise = 82
english_marks_premise = 47
biology_marks_premise = 85

math_marks_hypothesis = 86
science_marks_hypothesis = 65
social_studies_marks_hypothesis = 82
english_marks_hypothesis = 47
biology_marks_hypothesis = 85

# the hypothesis refers to the exact marks scored by Shekar in each subject mentioned in the premise
if math_marks_hypothesis != math_marks_premise:
    # check if the math marks in the hypothesis contradicts the math marks reported in the premise
    label = "contradiction"
elif science_marks_hypothesis != science_marks_premise or social_studies_marks_hypothesis != social_studies_marks_premise or english_marks_hypothesis != english_marks_premise or biology_marks_hypothesis != biology_marks_premise:
    # check if the marks in the other subjects in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
