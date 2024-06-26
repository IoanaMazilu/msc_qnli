departure_rate_premise = 60
departure_rate_hypothesis = 20

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_premise <= departure_rate_hypothesis:
    # check if the estimate of 'departure_rate_hypothesis' contradicts the departure rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
