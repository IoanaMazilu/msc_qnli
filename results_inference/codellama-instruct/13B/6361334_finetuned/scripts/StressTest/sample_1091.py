matthew_walking_rate_premise = 3
matthew_walking_rate_hypothesis = 4

# the hypothesis refers to the walking rates mentioned in the premise
if matthew_walking_rate_hypothesis <= matthew_walking_rate_premise:
    # check if the estimate of'matthew_walking_rate_hypothesis' contradicts the number of km walked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
