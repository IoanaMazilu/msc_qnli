ramesh_work_days_premise = 60
ramesh_work_days_hypothesis = 20
sushil_work_days_premise = 25
sushil_work_days_hypothesis = 25

# the hypothesis refers to the ability of Ramesh and Sushil to finish a work, mentioned also in the premise
if ramesh_work_days_hypothesis >= ramesh_work_days_premise:
    # check if the work days of 'ramesh_work_days_hypothesis' contradicts the premise (less than 'ramesh_work_days_premise')
    label = "contradiction"
elif sushil_work_days_hypothesis != sushil_work_days_premise:
    # check if the work days of Sushil in the hypothesis contradicts the work days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
