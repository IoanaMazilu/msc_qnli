ramesh_work_days_premise = 60
ramesh_work_days_hypothesis = 20
sushil_work_days_premise = 25
sushil_work_days_hypothesis = 25

# the hypothesis refers to the work days for Ramesh and Sushil mentioned in the premise
if ramesh_work_days_hypothesis >= ramesh_work_days_premise:
    # check if the estimated work days for Ramesh in the hypothesis contradicts the estimate of less than 'ramesh_work_days_premise'
    label = "contradiction"
elif sushil_work_days_hypothesis!= sushil_work_days_premise:
    # check if the number of work days for Sushil in the hypothesis contradicts the number of work days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
