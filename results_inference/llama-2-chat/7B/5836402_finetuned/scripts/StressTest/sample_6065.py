english_mark_premise = 86
english_mark_hypothesis = 56

mathematics_mark_premise = 89
mathematics_mark_hypothesis = 89

physics_mark_premise = 82
physics_mark_hypothesis = 82

chemistry_mark_premise = 87
chemistry_mark_hypothesis = 87

biology_mark_premise = 81
biology_mark_hypothesis = 81

# the hypothesis refers to the marks obtained by Dacid in each subject, mentioned in the premise
if english_mark_hypothesis!= english_mark_premise:
    # check if the English mark in the hypothesis contradicts the English mark reported in the premise
    label = "contradiction"
elif mathematics_mark_hypothesis!= mathematics_mark_premise:
    # check if the Mathematics mark in the hypothesis contradicts the Mathematics mark reported in the premise
    label = "contradiction"
elif physics_mark_hypothesis!= physics_mark_premise:
    # check if the Physics mark in the hypothesis contradicts the Physics mark reported in the premise
    label = "contradiction"
elif chemistry_mark_hypothesis!= chemistry_mark_premise:
    # check if the Chemistry mark in the hypothesis contradicts the Chemistry mark reported in the premise
    label = "contradiction"
elif biology_mark_hypothesis!= biology_mark_premise:
    # check if the Biology mark in the hypothesis contradicts the Biology mark reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
