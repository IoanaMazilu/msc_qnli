wales_score_premise = 51
scotland_score_premise = 3
wales_score_hypothesis = 51
scotland_score_hypothesis = 3

# the hypothesis mentions the score of the match between Wales and Scotland and their position above France, which are also mentioned in the premise
if wales_score_hypothesis != wales_score_premise:
    # check if the score of Wales in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif scotland_score_hypothesis != scotland_score_premise:
    # check if the score of Scotland from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
