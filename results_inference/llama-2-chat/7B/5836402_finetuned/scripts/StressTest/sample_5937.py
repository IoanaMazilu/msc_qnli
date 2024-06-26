employees_premise = 180
employees_hypothesis = 280

# the hypothesis refers to the number of employees at Veridux Corporation, mentioned in the premise
if employees_hypothesis >= employees_premise:
    # check if the estimate of 'employees_hypothesis' contradicts the number of employees in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
