departure_rate_premise = 50
departure_rate_hypothesis = 10

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis!= departure_rate_premise:
    # check if the on-time departure rate in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the on-time departure rate in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
