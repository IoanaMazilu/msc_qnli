ramesh_work_days_premise = 20
ramesh_work_days_hypothesis = 20
sushil_work_days_premise = 25
sushil_work_days_hypothesis = 25

# the hypothesis refers to the time Ramesh and Sushil need to finish a work, mentioned in the premise
if ramesh_work_days_hypothesis <= ramesh_work_days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ramesh_work_days_premise'
    label = "contradiction"
elif sushil_work_days_hypothesis!= sushil_work_days_premise:
    # check if the number of days Sushil needs to finish a work in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
