# Premise: Ramesh can finish a work in 20 days and Sushil in 25 days.
# Hypothesis: Ramesh can finish a work in less than 60 days and Sushil in 25 days.
# Golden Label: entailment

ramesh_work_days_premise = 20
sushil_work_days_premise = 25
ramesh_work_days_hypothesis = 60
sushil_work_days_hypothesis = 25

# the hypothesis refers to the working capability of Ramesh and Sushil mentioned in the premise
if ramesh_work_days_hypothesis < ramesh_work_days_premise:
    # check if the estimate of 'ramesh_work_days_hypothesis' contradicts the number of work days of Ramesh in the premise
    label = "contradiction"
elif sushil_work_days_hypothesis != sushil_work_days_premise:
    # check if the number of work days of Sushil in the hypothesis contradicts the number of work days of Sushil in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

