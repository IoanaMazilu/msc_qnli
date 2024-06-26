departure_rate_premise = 80
departure_rate_hypothesis = 20

# the hypothesis refers to the departure rate mentioned in the premise
if departure_rate_hypothesis > departure_rate_premise:
    # check if the hypothesis value contradicts the departure rate in the premise
    label = "contradiction"
elif departure_rate_hypothesis < departure_rate_premise:
    # check if the departure rate in the hypothesis is less than the premise
    # this would be consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value and premise are the same, we can infer entailment
    label = "entailment"

print(label)
