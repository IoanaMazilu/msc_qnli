napoli_score_premise = 6
napoli_score_hypothesis = 6

# the hypothesis mentions the Napoli score against Cagliari, which is also mentioned in the premise
if napoli_score_hypothesis!= napoli_score_premise:
    # check if the Napoli score in the hypothesis contradicts the Napoli score reported in the premise
    label = "contradiction"
else:
    # if the Napoli score in the hypothesis does not contradict the Napoli score in the premise, we can infer entailment
    label = "entailment"

print(label)
