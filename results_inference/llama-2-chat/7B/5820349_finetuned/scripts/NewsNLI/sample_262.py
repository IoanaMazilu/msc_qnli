napoli_score_premise = 6
napoli_place_premise = 4
napoli_score_hypothesis = 6
cagliari_score_hypothesis = 3
napoli_place_hypothesis = 4

# the hypothesis mentions the Napoli's score and their current place, which are also mentioned in the premise
# but the hypothesis does not mention the Cagliari's score
if napoli_score_hypothesis!= napoli_score_premise:
    # check if the Napoli's score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif napoli_place_hypothesis!= napoli_place_premise:
    # check if the Napoli's current place from the hypothesis contradicts their current place in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
