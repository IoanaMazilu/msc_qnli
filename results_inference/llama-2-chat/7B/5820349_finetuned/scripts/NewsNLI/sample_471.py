real_madrid_score_premise = 5
real_madrid_score_hypothesis = 5
real_murcia_score_premise = 1
real_murcia_score_hypothesis = 1

# the hypothesis mentions the score of the game, which is also mentioned in the premise
if real_madrid_score_hypothesis!= real_madrid_score_premise:
    # check if the score of Real Madrid in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif real_murcia_score_hypothesis!= real_murcia_score_premise:
    # check if the score of Real Murcia from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
