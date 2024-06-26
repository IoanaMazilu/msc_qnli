raman_travel_premise = 10
raman_travel_hypothesis = 10

# the hypothesis refers to the number of hours Raman travelled, mentioned in the premise
if raman_travel_hypothesis >= raman_travel_premise:
    # check if the estimate of 'raman_travel_hypothesis' contradicts the number of hours in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
