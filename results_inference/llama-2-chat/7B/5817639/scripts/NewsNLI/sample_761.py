passenger_premise = 1
passenger_hypothesis = 1

# the hypothesis mentions the amount paid by one passenger for a specific trip, which is also referenced in the premise
if passenger_hypothesis!= passenger_premise:
    # check if the amount paid by the passenger in the hypothesis contradicts the amount paid by the passenger in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
