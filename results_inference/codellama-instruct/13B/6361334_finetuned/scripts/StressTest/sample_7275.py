molly_max_rate_premise = 100
molly_max_rate_hypothesis = 400

# the hypothesis refers to the rate of driving mentioned in the premise
if molly_max_rate_hypothesis >= molly_max_rate_premise:
    # check if the estimate of'molly_max_rate_hypothesis' contradicts the rate of driving in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
