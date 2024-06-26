departure_rate_premise = 80
departure_rate_hypothesis = 70

# the hypothesis refers to the on-time departure rate percentage mentioned in the premise
if departure_rate_premise < departure_rate_hypothesis:
    # check if the estimate of 'departure_rate_hypothesis' contradicts the rate in the premise
    label = "contradiction"
elif departure_rate_hypothesis > departure_rate_premise:
    # check if the departure rate in the hypothesis is greater than the one stated in the premise
    label = "contradiction"
else:
    # if the departure rate in the hypothesis is equal to the one in the premise, we can infer entailment
    label = "entailment"

print(label)
