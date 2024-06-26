english_marks_premise = 76
mathematics_marks_premise = 65
physics_marks_premise = 82
chemistry_marks_premise = 67
biology_marks_premise = 85

english_marks_hypothesis = 76
mathematics_marks_hypothesis = 65
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 67
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by David in the same subjects as the premise
if english_marks_hypothesis >= english_marks_premise:
    # check if the hypothesis value contradicts the premise value for English marks
    label = "contradiction"
elif mathematics_marks_hypothesis >= mathematics_marks_premise:
    # check if the hypothesis value contradicts the premise value for Mathematics marks
    label = "contradiction"
elif physics_marks_hypothesis >= physics_marks_premise:
    # check if the hypothesis value contradicts the premise value for Physics marks
    label = "contradiction"
elif chemistry_marks_hypothesis >= chemistry_marks_premise:
    # check if the hypothesis value contradicts the premise value for Chemistry marks
    label = "contradiction"
elif biology_marks_hypothesis >= biology_marks_premise:
    # check if the hypothesis value contradicts the premise value for Biology marks
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
