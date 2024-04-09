departure_rate_premise = 70
departure_rate_hypothesis = 50

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis > departure_rate_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif departure_rate_hypothesis < departure_rate_premise:
    # if the hypothesis value is less than the premise value, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise value, it can be explicitly entailed from the premise
    label = "entailment"

print(label)
