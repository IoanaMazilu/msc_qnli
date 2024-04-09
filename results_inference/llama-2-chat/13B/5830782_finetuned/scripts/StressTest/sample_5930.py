english_mark_premise = 86
english_mark_hypothesis = 86
math_mark_premise = 85
math_mark_hypothesis = 85
physics_mark_premise = 92
physics_mark_hypothesis = 92
chemistry_mark_premise = 87
chemistry_mark_hypothesis = 87
biology_mark_premise = 95
biology_mark_hypothesis = 95

# the hypothesis refers to the marks obtained by Dacid in each subject mentioned in the premise
if english_mark_hypothesis >= english_mark_premise:
    # check if the hypothesis value contradicts the premise for English marks
    label = "contradiction"
elif math_mark_hypothesis!= math_mark_premise:
    # check if the hypothesis value contradicts the premise for Mathematics marks
    label = "contradiction"
elif physics_mark_hypothesis!= physics_mark_premise:
    # check if the hypothesis value contradicts the premise for Physics marks
    label = "contradiction"
elif chemistry_mark_hypothesis!= chemistry_mark_premise:
    # check if the hypothesis value contradicts the premise for Chemistry marks
    label = "contradiction"
elif biology_mark_hypothesis!= biology_mark_premise:
    # check if the hypothesis value contradicts the premise for Biology marks
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
