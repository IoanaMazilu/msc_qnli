score_premise = 0
score_hypothesis = 0

# the hypothesis mentions the score of the game and the result, which are also mentioned in the premise
if score_hypothesis != score_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis score does not contradict the premise score, we can infer entailment
    label = "entailment"

print(label)
