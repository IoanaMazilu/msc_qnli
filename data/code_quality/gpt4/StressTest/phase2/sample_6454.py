english_mark_premise = 76
english_mark_hypothesis = 66
math_mark_premise = math_mark_hypothesis = 60
chem_mark_premise = chem_mark_hypothesis = 72
bio_mark_premise = bio_mark_hypothesis = 77
french_mark_premise = french_mark_hypothesis = 55
physics_mark_premise = physics_mark_hypothesis = 85

# the hypothesis refers to the same examination marks mentioned in the premise
if english_mark_hypothesis >= english_mark_premise:
    # check if the English mark in the hypothesis contradicts the estimate of less than 'english_mark_premise'
    label = "contradiction"
elif math_mark_hypothesis != math_mark_premise or chem_mark_hypothesis != chem_mark_premise or bio_mark_hypothesis != bio_mark_premise or french_mark_hypothesis != french_mark_premise or physics_mark_hypothesis != physics_mark_premise:
    # check if any of the other marks in the hypothesis contradict the corresponding marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
