english_mark_premise = 86
mathematics_mark_premise = 86
physics_mark_premise = 82
chemistry_mark_premise = 82
biology_mark_premise = 85

english_mark_hypothesis = 86
mathematics_mark_hypothesis = 86
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 82
biology_mark_hypothesis = 85

# the hypothesis refers to the marks obtained by David in each subject mentioned in the premise
if english_mark_hypothesis <= english_mark_premise:
    # check if the hypothesis value contradicts the estimate of more than 'english_mark_premise'
    label = "contradiction"
elif mathematics_mark_hypothesis!= mathematics_mark_premise:
    # check if the mathematics mark in the hypothesis contradicts the mathematics mark reported in the premise
    label = "contradiction"
elif physics_mark_hypothesis!= physics_mark_premise:
    # check if the physics mark in the hypothesis contradicts the physics mark reported in the premise
    label = "contradiction"
elif chemistry_mark_hypothesis!= chemistry_mark_premise:
    # check if the chemistry mark in the hypothesis contradicts the chemistry mark reported in the premise
    label = "contradiction"
elif biology_mark_hypothesis!= biology_mark_premise:
    # check if the biology mark in the hypothesis contradicts the biology mark reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
