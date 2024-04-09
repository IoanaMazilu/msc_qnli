english_mark_premise = 16
math_mark_premise = 95
physics_mark_premise = 82
chemistry_mark_premise = 87
biology_mark_premise = 92

english_mark_hypothesis = 96
math_mark_hypothesis = 95
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 87
biology_mark_hypothesis = 92

# the hypothesis refers to the marks obtained by Dacid in different subjects mentioned in the premise
if english_mark_hypothesis <= english_mark_premise:
    # check if the English mark in the hypothesis contradicts the estimate of more than 'english_mark_premise'
    label = "contradiction"
elif math_mark_hypothesis!= math_mark_premise or physics_mark_hypothesis!= physics_mark_premise or chemistry_mark_hypothesis!= chemistry_mark_premise or biology_mark_hypothesis!= biology_mark_premise:
    # check if any of the other marks in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the English mark
    # any mark in English greater than 'english_mark_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
