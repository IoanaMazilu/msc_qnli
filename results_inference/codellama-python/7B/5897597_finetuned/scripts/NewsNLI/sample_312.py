score_premise = 4
score_hypothesis = 4

# the hypothesis mentions the score of the game, which is also mentioned in the premise
if score_hypothesis!= score_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the score in the hypothesis does not contradict the score in the premise, we can infer entailment
    label = "entailment"

print(label)
