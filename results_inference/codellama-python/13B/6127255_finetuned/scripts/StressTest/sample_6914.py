departure_rate_premise = 70
departure_rate_hypothesis = 50

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis >= departure_rate_premise:
    # check if the 'departure_rate_hypothesis' contradicts the departure rate in the premise
    label = "contradiction"
else:
    # if the departure rate in the hypothesis is less than the one in the premise, we can infer entailment
    label = "entailment"

print(label)
