english_mark_premise = 86
math_mark_premise = 89
physics_mark_premise = 82
chemistry_mark_premise = 87
biology_mark_premise = 81

english_mark_hypothesis = 56
math_mark_hypothesis = 89
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 87
biology_mark_hypothesis = 81

# the hypothesis refers to the marks obtained by Dacid in various subjects mentioned in the premise
if english_mark_hypothesis!= english_mark_premise:
    # check if the English mark in the hypothesis contradicts the English mark reported in the premise
    label = "contradiction"
elif math_mark_hypothesis!= math_mark_premise or physics_mark_hypothesis!= physics_mark_premise or chemistry_mark_hypothesis!= chemistry_mark_premise or biology_mark_hypothesis!= biology_mark_premise:
    # check if the marks in other subjects in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
