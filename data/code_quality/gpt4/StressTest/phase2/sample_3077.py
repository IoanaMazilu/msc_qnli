english_mark_premise = 51
english_mark_hypothesis = 71
math_mark_premise = 65
math_mark_hypothesis = 65
physics_mark_premise = 82
physics_mark_hypothesis = 82
chemistry_mark_premise = 67
chemistry_mark_hypothesis = 67
biology_mark_premise = 85
biology_mark_hypothesis = 85

# the hypothesis refers to the marks obtained by Dacid in each of the subjects mentioned in the premise
if english_mark_hypothesis != english_mark_premise:
    # check if the English mark in the hypothesis contradicts the English mark in the premise
    label = "contradiction"
elif math_mark_hypothesis != math_mark_premise:
    # check if the Math mark in the hypothesis contradicts the Math mark in the premise
    label = "contradiction"
elif physics_mark_hypothesis != physics_mark_premise:
    # check if the Physics mark in the hypothesis contradicts the Physics mark in the premise
    label = "contradiction"
elif chemistry_mark_hypothesis != chemistry_mark_premise:
    # check if the Chemistry mark in the hypothesis contradicts the Chemistry mark in the premise
    label = "contradiction"
elif biology_mark_hypothesis != biology_mark_premise:
    # check if the Biology mark in the hypothesis contradicts the Biology mark in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
