departure_rate_premise = 50
departure_rate_hypothesis = 10

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis > departure_rate_premise:
    # check if the 'departure_rate_hypothesis' contradicts the 'departure_rate_premise'
    label = "contradiction"
elif departure_rate_hypothesis < departure_rate_premise:
    # check if the 'departure_rate_hypothesis' is less than the 'departure_rate_premise'
    label = "entailment"
else:
    # if the departure rates are equal, we can infer neutrality
    label = "neutral"

print(label)
