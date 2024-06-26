napoli_score_premise = 6
napoli_score_hypothesis = 6

# the hypothesis mentions Napoli's score and their position, which are also mentioned in the premise
if napoli_score_hypothesis!= napoli_score_premise:
    # check if the Napoli's score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
