ramesh_days_premise = 20
ramesh_days_hypothesis = 20
sushil_days_premise = 25
sushil_days_hypothesis = 25

# the hypothesis refers to the number of days it takes for Ramesh and Sushil to finish a work
if ramesh_days_hypothesis <= ramesh_days_premise:
    # check if the estimate of 'ramesh_days_hypothesis' contradicts the number of days it takes for Ramesh in the premise
    label = "contradiction"
elif sushil_days_hypothesis!= sushil_days_premise:
    # check if the number of days it takes for Sushil in the hypothesis contradicts the number of days it takes for Sushil reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
