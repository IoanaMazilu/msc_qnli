english_marks_premise = 46
math_marks_premise = 95
physics_marks_premise = 82
chemistry_marks_premise = 97
biology_marks_premise = 95

english_marks_hypothesis = 96
math_marks_hypothesis = 95
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 97
biology_marks_hypothesis = 95

# the hypothesis refers to the marks obtained by Dacid in different subjects mentioned in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the mark in English in the hypothesis contradicts the mark in the premise
    label = "contradiction"
elif math_marks_hypothesis != math_marks_premise:
    # check if the mark in Mathematics in the hypothesis contradicts the mark in the premise
    label = "contradiction"
elif physics_marks_hypothesis != physics_marks_premise:
    # check if the mark in Physics in the hypothesis contradicts the mark in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis != chemistry_marks_premise:
    # check if the mark in Chemistry in the hypothesis contradicts the mark in the premise
    label = "contradiction"
elif biology_marks_hypothesis != biology_marks_premise:
    # check if the mark in Biology in the hypothesis contradicts the mark in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
