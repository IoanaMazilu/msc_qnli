season_premise = 10
season_hypothesis = 10

# the hypothesis mentions the number of season in the United States, which is also mentioned in the premise
if season_hypothesis!= season_premise:
    # check if the season in the hypothesis contradicts the season reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
