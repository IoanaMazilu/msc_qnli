english_mark_premise = 76
english_mark_hypothesis = 86
mathematics_mark_premise = 65
mathematics_mark_hypothesis = 65
physics_mark_premise = 82
physics_mark_hypothesis = 82
chemistry_mark_premise = 67
chemistry_mark_hypothesis = 67
biology_mark_premise = 85
biology_mark_hypothesis = 85

# the hypothesis refers to the marks obtained by David in English, mathematics, physics, chemistry and biology
if english_mark_hypothesis <= english_mark_premise:
    # check if the hypothesis value contradicts the premise value for English mark
    label = "contradiction"
elif mathematics_mark_hypothesis!= mathematics_mark_premise:
    # check if the hypothesis value contradicts the premise value for mathematics mark
    label = "contradiction"
elif physics_mark_hypothesis!= physics_mark_premise:
    # check if the hypothesis value contradicts the premise value for physics mark
    label = "contradiction"
elif chemistry_mark_hypothesis!= chemistry_mark_premise:
    # check if the hypothesis value contradicts the premise value for chemistry mark
    label = "contradiction"
elif biology_mark_hypothesis!= biology_mark_premise:
    # check if the hypothesis value contradicts the premise value for biology mark
    label = "contradiction"
else:
    # if the hypothesis values and marks do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
