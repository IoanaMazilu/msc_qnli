departure_rate_premise = 70
departure_rate_hypothesis = 50

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis > departure_rate_premise:
    # check if the hypothesis value contradicts the estimated on-time departure rate in the premise
    label = "contradiction"
elif departure_rate_hypothesis < departure_rate_premise:
    # check if the hypothesis value is less than the estimated on-time departure rate in the premise
    label = "entailment"
else:
    # if the hypothesis value and the premise value are equal, we can infer entailment
    label = "entailment"

print(label)
