wales_score_premise = 3
wales_score_hypothesis = 3
scotland_score_premise = 0
scotland_score_hypothesis = 0
france_score_premise = 2
france_score_hypothesis = 2

# the hypothesis mentions the scores of Wales, Scotland and France, which are also mentioned in the premise
if wales_score_hypothesis!= wales_score_premise:
    # check if the score of Wales in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif scotland_score_hypothesis!= scotland_score_premise:
    # check if the score of Scotland from the hypothesis contradicts the score in the premise
    label = "contradiction"
elif france_score_hypothesis!= france_score_premise:
    # check if the score of France from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
