floors_premise = 71
floors_hypothesis = 51
rate_per_minute_premise = 93

# the hypothesis refers to the floor and rate mentioned in the premise
if floors_hypothesis <= floors_premise:
    # check if the estimate of 'floors_hypothesis' contradicts the floor reported in the premise
    label = "contradiction"
elif rate_per_minute_premise!= rate_per_minute_hypothesis:
    # check if the rate per minute in the hypothesis contradicts the rate per minute reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
