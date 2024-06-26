matthew_walking_rate_premise = 5
matthew_walking_rate_hypothesis = 3
johnny_walking_rate_premise = 4
johnny_walking_rate_hypothesis = 4

# the hypothesis refers to the walking rates mentioned in the premise
if matthew_walking_rate_hypothesis >= matthew_walking_rate_premise:
    # check if the estimate of'matthew_walking_rate_hypothesis' contradicts the number of cookie sales in the premise
    label = "contradiction"
elif johnny_walking_rate_hypothesis!= johnny_walking_rate_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
