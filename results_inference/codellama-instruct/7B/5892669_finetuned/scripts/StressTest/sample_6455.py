english_score_premise = 66
english_score_hypothesis = 66
math_score_premise = 60
math_score_hypothesis = 60
chem_score_premise = 72
chem_score_hypothesis = 72
bio_score_premise = 77
bio_score_hypothesis = 77
french_score_premise = 55
french_score_hypothesis = 55
physics_score_premise = 85
physics_score_hypothesis = 85

# the hypothesis refers to the scores Andrea got in different subjects mentioned in the premise
if english_score_hypothesis >= english_score_premise:
    # check if the estimate of 'english_score_hypothesis' contradicts the English score in the premise
    label = "contradiction"
elif math_score_hypothesis!= math_score_premise or chem_score_hypothesis!= chem_score_premise or bio_score_hypothesis!= bio_score_premise or french_score_hypothesis!= french_score_premise or physics_score_hypothesis!= physics_score_premise:
    # check if the scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
