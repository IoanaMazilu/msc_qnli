departure_rate_premise = 80
departure_rate_hypothesis = 80

# the hypothesis refers to the on-time departure rate from Phoenix (which is also referenced in the premise)
if departure_rate_hypothesis != departure_rate_premise:
    # check if the departure rate value in the hypothesis contradicts the departure rate value in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
