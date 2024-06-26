switzerland_points_premise = 3
ecuador_points_premise = 3
ecuador_honduras_score_premise = [2, 1]

ecuador_honduras_score_hypothesis = [2, 1]

# the hypothesis mentions the result of the Ecuador-Honduras game, which is also mentioned in the premise
if ecuador_honduras_score_premise != ecuador_honduras_score_hypothesis:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
