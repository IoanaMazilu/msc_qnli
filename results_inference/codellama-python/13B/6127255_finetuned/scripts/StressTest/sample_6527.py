departure_rate_premise = 60
departure_rate_hypothesis = 20

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis > departure_rate_premise:
    # check if the 'departure_rate_hypothesis' contradicts the departure rate in the premise
    label = "contradiction"
elif departure_rate_hypothesis < departure_rate_premise:
    # check if the 'departure_rate_hypothesis' is less than the departure rate in the premise
    label = "entailment"
else:
    # if the departure rate in the hypothesis is equal to the one in the premise, we can infer neutrality
    label = "neutral"

print(label)
