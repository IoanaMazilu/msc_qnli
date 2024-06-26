work_days_premise = 40
work_days_hypothesis = 20
rajesh_days_premise = 30
rajesh_days_hypothesis = 30

# the hypothesis refers to the number of days he works and the number of days Rajesh finishes it
if work_days_hypothesis >= work_days_premise:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of days he works in the premise
    label = "contradiction"
elif rajesh_days_hypothesis!= rajesh_days_premise:
    # check if the number of days Rajesh finishes in the hypothesis contradicts the number of days Rajesh finishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
