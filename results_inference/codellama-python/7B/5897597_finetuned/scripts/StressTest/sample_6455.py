english_mark_premise = 66
math_mark_premise = 60
chemistry_mark_premise = 72
biology_mark_premise = 77
french_mark_premise = 55
physics_mark_premise = 85

english_mark_hypothesis = 66
math_mark_hypothesis = 60
chemistry_mark_hypothesis = 72
biology_mark_hypothesis = 77
french_mark_hypothesis = 55
physics_mark_hypothesis = 85

# the hypothesis refers to the marks scored by Andrea in various subjects mentioned in the premise
if english_mark_hypothesis >= english_mark_premise:
    # check if the hypothesis value contradicts the premise value for English mark
    label = "contradiction"
elif math_mark_hypothesis!= math_mark_premise or chemistry_mark_hypothesis!= chemistry_mark_premise or biology_mark_hypothesis!= biology_mark_premise or french_mark_hypothesis!= french_mark_premise or physics_mark_hypothesis!= physics_mark_premise:
    # check if the hypothesis values for the other subjects contradict the premise values for the same subjects
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
