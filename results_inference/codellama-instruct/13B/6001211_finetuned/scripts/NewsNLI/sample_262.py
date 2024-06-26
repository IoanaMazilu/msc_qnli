napoli_score_premise = 6
cagliari_score_premise = 3
napoli_score_hypothesis = 6

# the hypothesis mentions Napoli's score and the move to fourth place, which are also mentioned in the premise
if napoli_score_hypothesis!= napoli_score_premise:
    # check if the Napoli's score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the Napoli's score in the hypothesis does not contradict the score in the premise, we can infer entailment
    label = "entailment"

print(label)
