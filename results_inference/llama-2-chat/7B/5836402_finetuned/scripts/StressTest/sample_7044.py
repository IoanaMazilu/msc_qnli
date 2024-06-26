travel_hours_premise = 10
travel_hours_hypothesis = 20

# the hypothesis refers to the number of hours Raman travelled, which is also mentioned in the premise
if travel_hours_hypothesis >= travel_hours_premise:
    # check if the hypothesis value contradicts the number of hours travelled in the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the number of hours travelled in the premise, we can infer entailment
    label = "entailment"

print(label)
