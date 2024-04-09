departure_rate_premise = 80
departure_rate_hypothesis = 70

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis >= departure_rate_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
