ramesh_work_days_premise = 20
ramesh_work_days_hypothesis = 20
sushil_work_days_premise = 25
sushil_work_days_hypothesis = 25

# the hypothesis refers to the number of days Ramesh and Sushil need to finish a work, mentioned in the premise
if ramesh_work_days_hypothesis <= ramesh_work_days_premise:
    # check if the hypothesis value contradicts the number of days Ramesh needs in the premise
    label = "contradiction"
elif sushil_work_days_hypothesis!= sushil_work_days_premise:
    # check if the number of days Sushil needs in the hypothesis contradicts the number of days Sushil needs in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
