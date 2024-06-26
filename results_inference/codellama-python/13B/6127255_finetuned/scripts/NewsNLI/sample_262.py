napoli_score_premise = 6
cagliari_score_premise = 3
napoli_score_hypothesis = 6
napoli_position_premise = 4
napoli_position_hypothesis = 4

# the hypothesis mentions Napoli's score and position, which are also mentioned in the premise
if napoli_score_hypothesis!= napoli_score_premise:
    # check if the score of Napoli in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif napoli_position_hypothesis!= napoli_position_premise:
    # check if the position of Napoli from the hypothesis contradicts the position of Napoli in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
