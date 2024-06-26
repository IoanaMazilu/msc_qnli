work_days_premise = 20
work_days_hypothesis = 60
rajesh_work_days_premise = 30
rajesh_work_days_hypothesis = 30

# the hypothesis refers to the number of days he worked and the number of days Rajesh worked, mentioned in the premise
if work_days_premise >= work_days_hypothesis:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
elif rajesh_work_days_hypothesis != rajesh_work_days_premise:
    # check if the number of days Rajesh worked in the hypothesis contradicts the number of days Rajesh worked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
