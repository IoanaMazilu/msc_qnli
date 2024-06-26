departure_rate_premise = 40
departure_rate_hypothesis = 60

# the hypothesis refers to the departure rate mentioned in the premise
if departure_rate_hypothesis <= departure_rate_premise:
    # check if the departure rate in the hypothesis contradicts the departure rate in the premise
    label = "contradiction"
elif departure_rate_hypothesis > departure_rate_premise:
    # if the departure rate in the hypothesis is greater than the departure rate in the premise, it is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
