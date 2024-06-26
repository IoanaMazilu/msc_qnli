ramesh_work_days_premise = 60
ramesh_work_days_hypothesis = 20
sushil_work_days_premise = 25
sushil_work_days_hypothesis = 25

# the hypothesis refers to the number of days Ramesh and Sushil need to finish a work, mentioned in the premise
if ramesh_work_days_hypothesis >= ramesh_work_days_premise:
    # check if the number of days Ramesh needs to finish a work in the hypothesis contradicts the premise
    label = "contradiction"
elif sushil_work_days_hypothesis!= sushil_work_days_premise:
    # check if the number of days Sushil needs to finish a work in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
