distance_premise = 100
distance_hypothesis = 300
rate_premise = 50
rate_hypothesis = 50

# the hypothesis talks about the distance and rate of a train travel, also mentioned in the premise
if distance_hypothesis < distance_premise or rate_hypothesis != rate_premise:
    # check if the distance or rate in the hypothesis contradicts the distance or rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
