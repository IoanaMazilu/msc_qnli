departure_rate_premise = 40
departure_rate_hypothesis = 80

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis >= departure_rate_premise:
    # check if the estimate of 'departure_rate_hypothesis' contradicts the on-time departure rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
