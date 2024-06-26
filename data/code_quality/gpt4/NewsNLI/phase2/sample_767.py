start_score_premise = -2
start_score_hypothesis = -2

# the hypothesis mentions the starting score in the series, which is also mentioned in the premise
# it also refers to the illegal modification of the catamarans which is a shared detail between the premise and the hypothesis
if start_score_hypothesis != start_score_premise:
    # check if the starting score in the hypothesis contradicts the starting score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
