english_mark_premise = 76
english_mark_hypothesis = 46
mathematics_mark_premise = 65
mathematics_mark_hypothesis = 65
chemistry_mark_premise = 82
chemistry_mark_hypothesis = 82
biology_mark_premise = 67
biology_mark_hypothesis = 67
physics_mark_premise = 85
physics_mark_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in each subject mentioned in the premise
if english_mark_hypothesis!= english_mark_premise:
    # check if the English mark in the hypothesis contradicts the English mark reported in the premise
    label = "contradiction"
elif mathematics_mark_hypothesis!= mathematics_mark_premise:
    # check if the Mathematics mark in the hypothesis contradicts the Mathematics mark reported in the premise
    label = "contradiction"
elif chemistry_mark_hypothesis!= chemistry_mark_premise:
    # check if the Chemistry mark in the hypothesis contradicts the Chemistry mark reported in the premise
    label = "contradiction"
elif biology_mark_hypothesis!= biology_mark_premise:
    # check if the Biology mark in the hypothesis contradicts the Biology mark reported in the premise
    label = "contradiction"
elif physics_mark_hypothesis!= physics_mark_premise:
    # check if the Physics mark in the hypothesis contradicts the Physics mark reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
