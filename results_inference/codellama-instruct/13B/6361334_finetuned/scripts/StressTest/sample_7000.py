ramesh_days_premise = 60
ramesh_days_hypothesis = 20
sushil_days_premise = 25
sushil_days_hypothesis = 25

# the hypothesis refers to the number of days it takes to finish a work for Ramesh and Sushil, mentioned in the premise
if ramesh_days_hypothesis >= ramesh_days_premise:
    # check if the estimate of 'ramesh_days_hypothesis' contradicts the number of days it takes for Ramesh to finish a work in the premise
    label = "contradiction"
elif sushil_days_hypothesis!= sushil_days_premise:
    # check if the number of days it takes for Sushil to finish a work in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
