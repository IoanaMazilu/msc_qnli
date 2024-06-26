departure_rate_premise = 60
departure_rate_hypothesis = 40

# the hypothesis refers to the on-time departure rate from Phoenix mentioned in the premise
if departure_rate_premise < departure_rate_hypothesis:
    # check if the 'departure_rate_hypothesis' contradicts the on-time departure rate in the premise
    label = "contradiction"
elif departure_rate_hypothesis < departure_rate_premise:
    # check if the on-time departure rate in the hypothesis can be inferred from the on-time departure rate reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutral
    label = "neutral"

print(label)
