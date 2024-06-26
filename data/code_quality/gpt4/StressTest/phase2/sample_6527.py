departure_rate_premise = 60
departure_rate_hypothesis = 20

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis > departure_rate_premise:
    # check if the 'departure_rate_hypothesis' contradicts the departure rate in the premise
    label = "contradiction"
elif departure_rate_hypothesis < departure_rate_premise:
    # check if the 'departure_rate_hypothesis' is lower than the departure rate in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
