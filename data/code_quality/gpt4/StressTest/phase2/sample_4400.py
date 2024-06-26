work_days_premise = 20
work_days_hypothesis = 10
rajesh_days_premise = 30
rajesh_days_hypothesis = 30

# the hypothesis refers to the number of work days and the number of days Rajesh worked, both mentioned in the premise
if work_days_hypothesis != work_days_premise:
    # check if the number of work days in the hypothesis contradicts the number of work days reported in the premise
    label = "contradiction"
elif rajesh_days_hypothesis != rajesh_days_premise:
    # check if the number of days Rajesh worked in the hypothesis contradicts the number of days Rajesh worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
