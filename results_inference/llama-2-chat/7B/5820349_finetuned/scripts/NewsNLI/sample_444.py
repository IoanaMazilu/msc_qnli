wales_rank_premise = 3
wales_rank_hypothesis = 3
france_rank_premise = 1
france_rank_hypothesis = 1
score_premise = 51
score_hypothesis = 51
scotland_rank_premise = 2
scotland_rank_hypothesis = 2

# the hypothesis mentions the rank of Wales, France, and Scotland, as well as the score of the game
# these are also mentioned in the premise
if wales_rank_hypothesis!= wales_rank_premise:
    # check if the rank of Wales in the hypothesis contradicts the rank of Wales in the premise
    label = "contradiction"
elif france_rank_hypothesis!= france_rank_premise:
    # check if the rank of France from the hypothesis contradicts the rank of France in the premise
    label = "contradiction"
elif score_hypothesis!= score_premise:
    # check if the score from the hypothesis contradicts the score in the premise
    label = "contradiction"
elif scotland_rank_hypothesis!= scotland_rank_premise:
    # check if the rank of Scotland from the hypothesis contradicts the rank of Scotland in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
