west_ham_score_premise = 3
west_ham_score_hypothesis = 3
west_brom_score_premise = 0
west_brom_score_hypothesis = 3

# the hypothesis mentions the final score of the game, which is also referenced in the premise
# however, the hypothesis refers to the West Ham's score after the half-time, which cannot be entailed from the premise
if west_ham_score_hypothesis!= west_ham_score_premise:
    # check if the final score in the hypothesis contradicts the final score reported in the premise
    label = "contradiction"
elif west_brom_score_hypothesis!= west_brom_score_premise:
    # check if the West Brom's score from the hypothesis contradicts the West Brom's score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
