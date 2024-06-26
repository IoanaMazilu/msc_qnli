english_mark_premise = 66
english_mark_hypothesis = 76
math_mark_premise = 60
math_mark_hypothesis = 60
chemistry_mark_premise = 72
chemistry_mark_hypothesis = 72
biology_mark_premise = 77
biology_mark_hypothesis = 77
french_mark_premise = 55
french_mark_hypothesis = 55
physics_mark_premise = 85
physics_mark_hypothesis = 85

# the hypothesis refers to the marks scored by Andrea in various subjects mentioned in the premise
if english_mark_hypothesis <= english_mark_premise:
    # check if the estimate of 'english_mark_hypothesis' contradicts the English mark in the premise
    label = "contradiction"
elif math_mark_hypothesis!= math_mark_premise:
    # check if the Math mark in the hypothesis contradicts the Math mark reported in the premise
    label = "contradiction"
elif chemistry_mark_hypothesis!= chemistry_mark_premise:
    # check if the Chemistry mark in the hypothesis contradicts the Chemistry mark reported in the premise
    label = "contradiction"
elif biology_mark_hypothesis!= biology_mark_premise:
    # check if the Biology mark in the hypothesis contradicts the Biology mark reported in the premise
    label = "contradiction"
elif french_mark_hypothesis!= french_mark_premise:
    # check if the French mark in the hypothesis contradicts the French mark reported in the premise
    label = "contradiction"
elif physics_mark_hypothesis!= physics_mark_premise:
    # check if the Physics mark in the hypothesis contradicts the Physics mark reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
