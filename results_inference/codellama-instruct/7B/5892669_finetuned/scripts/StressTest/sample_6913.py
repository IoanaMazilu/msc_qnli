departure_rate_premise = 80
departure_rate_hypothesis = 70

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis >= departure_rate_premise:
    # check if the 'departure_rate_hypothesis' contradicts the premise's upper limit
    label = "contradiction"
elif departure_rate_hypothesis < departure_rate_premise:
    # check if the 'departure_rate_hypothesis' is less than the premise's upper limit
    label = "entailment"
else:
    # if the hypothesis value does not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
