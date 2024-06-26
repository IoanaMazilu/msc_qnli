wales_score_premise = 51
scotland_score_premise = 3
wales_score_hypothesis = 51
scotland_score_hypothesis = 3

# the hypothesis mentions the score of Wales and Scotland, which are also mentioned in the premise
if wales_score_hypothesis!= wales_score_premise:
    # check if the score of Wales in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif scotland_score_hypothesis!= scotland_score_premise:
    # check if the score of Scotland from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
