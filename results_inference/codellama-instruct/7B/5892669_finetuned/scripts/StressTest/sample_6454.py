english_score_premise = 76
english_score_hypothesis = 66
math_score = 60
chem_score = 72
bio_score = 77
french_score = 55
physics_score = 85

# the hypothesis refers to the scores Andrea got in different subjects mentioned in the premise
if english_score_hypothesis >= english_score_premise:
    # check if the English score in the hypothesis contradicts the estimate of less than 'english_score_premise'
    label = "contradiction"
elif math_score!= 60 or chem_score!= 72 or bio_score!= 77 or french_score!= 55 or physics_score!= 85:
    # check if the scores in other subjects in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the English score
    # any English score less than 'english_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
