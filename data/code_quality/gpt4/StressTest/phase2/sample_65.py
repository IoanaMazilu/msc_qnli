work_days_premise = 20
work_days_hypothesis = 50
rajesh_days_premise = 30
rajesh_days_hypothesis = 30

# the hypothesis refers to the work days and Rajesh's work days mentioned in the premise
if work_days_premise != work_days_hypothesis:
    # check if the number of work days in the hypothesis contradicts the number of work days reported in the premise
    label = "contradiction"
elif rajesh_days_hypothesis != rajesh_days_premise:
    # check if Rajesh's work days in the hypothesis contradicts Rajesh's work days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
