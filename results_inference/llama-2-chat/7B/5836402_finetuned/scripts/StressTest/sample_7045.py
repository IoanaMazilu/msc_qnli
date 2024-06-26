travel_hours_premise = 20
travel_hours_hypothesis = 10

# the hypothesis refers to the number of hours Raman travelled, mentioned in the premise
if travel_hours_hypothesis >= travel_hours_premise:
    # check if the estimate of 'travel_hours_hypothesis' contradicts the number of hours Raman travelled in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
