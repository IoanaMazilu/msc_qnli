english_marks_premise = 76
mathematics_marks_premise = 65
chemistry_marks_premise = 82
biology_marks_premise = 67
physics_marks_premise = 85

english_marks_hypothesis = 46
mathematics_marks_hypothesis = 65
chemistry_marks_hypothesis = 82
biology_marks_hypothesis = 67
physics_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in different subjects
# we need to check if the marks in each subject in the hypothesis contradict the marks in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the hypothesis value for English marks contradicts the premise value
    label = "contradiction"
elif mathematics_marks_hypothesis <= mathematics_marks_premise:
    # check if the hypothesis value for Mathematics marks contradicts the premise value
    label = "contradiction"
elif chemistry_marks_hypothesis <= chemistry_marks_premise:
    # check if the hypothesis value for Chemistry marks contradicts the premise value
    label = "contradiction"
elif biology_marks_hypothesis <= biology_marks_premise:
    # check if the hypothesis value for Biology marks contradicts the premise value
    label = "contradiction"
elif physics_marks_hypothesis <= physics_marks_premise:
    # check if the hypothesis value for Physics marks contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
