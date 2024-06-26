ramesh_work_days_premise = 10
ramesh_work_days_hypothesis = 20
sushil_work_days_premise = 25
sushil_work_days_hypothesis = 25

# the hypothesis refers to the number of days Ramesh and Sushil can finish a work, mentioned in the premise
if ramesh_work_days_hypothesis <= ramesh_work_days_premise:
    # check if the number of 'ramesh_work_days_hypothesis' contradicts the premise of more than 'ramesh_work_days_premise' days
    label = "contradiction"
elif sushil_work_days_hypothesis != sushil_work_days_premise:
    # check if the number of 'sushil_work_days_hypothesis' contradicts the number of 'sushil_work_days_premise' mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Ramesh can finish a work
    # any number of days greater than 'ramesh_work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
