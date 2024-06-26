departure_rate_premise = 40
departure_rate_hypothesis = 50

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_premise >= departure_rate_hypothesis:
    # check if the estimate of 'departure_rate_hypothesis' contradicts the departure rate in the premise
    label = "contradiction"
else:
    # if the departure rate in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
