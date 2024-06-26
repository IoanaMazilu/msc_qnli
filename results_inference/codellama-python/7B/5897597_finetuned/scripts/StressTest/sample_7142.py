departure_rate_premise = 50
departure_rate_hypothesis = 10

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis > departure_rate_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif departure_rate_hypothesis < departure_rate_premise:
    # check if the hypothesis value is less than the premise value
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, we can infer neutrality
    label = "neutral"

print(label)
