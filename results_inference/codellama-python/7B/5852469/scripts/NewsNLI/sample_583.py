economy_growth_premise = 0.025
economy_growth_hypothesis = 0.025

# the hypothesis mentions the economic growth in the U.S., which is also mentioned in the premise
if economy_growth_hypothesis!= economy_growth_premise:
    # check if the economic growth in the hypothesis contradicts the economic growth in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
