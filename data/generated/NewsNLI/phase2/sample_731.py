# Premise: Molinari came flying out of the traps carding six birdies in the opening six holes but after such an impressive start he managed only one more in his round of 65.
# Hypothesis: Edaordo Molinari joins Jimenez on 11-under after round of 65.
# Golden Label: neutral

round_score_premise = 65
round_score_hypothesis = 65

# the hypothesis mentions the round score of Molinari, which is also referenced in the premise
if round_score_hypothesis != round_score_premise:
    # check if the round score in the hypothesis contradicts the round score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

