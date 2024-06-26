mexico_score_premise = 5
new_zealand_score_premise = 1
mexico_score_hypothesis = 5
new_zealand_score_hypothesis = 1

# the hypothesis mentions the score of Mexico's game against New Zealand, which is also mentioned in the premise
if mexico_score_hypothesis!= mexico_score_premise:
    # check if the score of Mexico in the hypothesis contradicts the score of Mexico reported in the premise
    label = "contradiction"
elif new_zealand_score_hypothesis!= new_zealand_score_premise:
    # check if the score of New Zealand from the hypothesis contradicts the score of New Zealand in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
