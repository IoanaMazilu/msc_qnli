score_spain_premise = 2
score_serbia_premise = 0
score_spain_hypothesis = 2
score_serbia_hypothesis = 0

# the hypothesis mentions the game score, which is also mentioned in the premise
if score_spain_hypothesis != score_spain_premise:
    # check if the score of Spain in the hypothesis contradicts the score of Spain reported in the premise
    label = "contradiction"
elif score_serbia_hypothesis != score_serbia_premise:
    # check if the score of Serbia from the hypothesis contradicts the score of Serbia in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
