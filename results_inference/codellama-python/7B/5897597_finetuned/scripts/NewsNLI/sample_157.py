west_ham_score_premise = 0
west_ham_score_hypothesis = 3
west_brom_score_premise = 0
west_brom_score_hypothesis = 3

# the hypothesis mentions the final score of West Ham and West Brom, which are also mentioned in the premise
if west_ham_score_hypothesis!= west_ham_score_premise:
    # check if the score of West Ham in the hypothesis contradicts the score of West Ham in the premise
    label = "contradiction"
elif west_brom_score_hypothesis!= west_brom_score_premise:
    # check if the score of West Brom from the hypothesis contradicts the score of West Brom in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
