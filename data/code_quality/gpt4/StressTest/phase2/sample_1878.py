travel_hours_premise = 11
travel_hours_hypothesis = 31

# the hypothesis indicates a maximum travel time for Pavan, compared to a specific travel time in the premise
if travel_hours_premise >= travel_hours_hypothesis:
    # check if the actual travel hours in the premise contradict the upper limit of travel hours in the hypothesis
    label = "contradiction"
else:
    # if the actual travel hours do not contradict the upper limit in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
