departure_rate_premise = 60
departure_rate_hypothesis = 20

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis > departure_rate_premise:
    # check if the 'departure_rate_hypothesis' contradicts the 'departure_rate_premise'
    label = "contradiction"
elif departure_rate_hypothesis == departure_rate_premise:
    # check if the 'departure_rate_hypothesis' is equal to the 'departure_rate_premise'
    label = "entailment"
else:
    # if the 'departure_rate_hypothesis' is less than the 'departure_rate_premise', it does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
