english_mark_premise = 96
english_mark_hypothesis = 46
math_mark_premise = 95
math_mark_hypothesis = 95
physics_mark_premise = 82
physics_mark_hypothesis = 82
chemistry_mark_premise = 97
chemistry_mark_hypothesis = 97
biology_mark_premise = 95
biology_mark_hypothesis = 95

# the hypothesis refers to the marks obtained by David in various subjects mentioned in the premise
if english_mark_hypothesis > english_mark_premise:
    # check if the mark in English in the hypothesis contradicts the mark in English in the premise
    label = "contradiction"
elif math_mark_hypothesis != math_mark_premise or physics_mark_hypothesis != physics_mark_premise or chemistry_mark_hypothesis != chemistry_mark_premise or biology_mark_hypothesis != biology_mark_premise:
    # check if the marks in Mathematics, Physics, Chemistry, or Biology in the hypothesis contradict the respective marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
