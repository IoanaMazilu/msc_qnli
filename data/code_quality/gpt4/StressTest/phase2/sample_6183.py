employees_premise = 218
employees_hypothesis = 818

# the hypothesis refers to the number of employees at Veridux Corporation mentioned in the premise
if employees_premise >= employees_hypothesis:
    # check if the number of employees in the premise contradicts the hypothesis estimate of less than 'employees_hypothesis'
    label = "contradiction"
else:
    # if the premise values and estimates do not contradict the hypothesis ones, we can infer entailment
    label = "entailment"

print(label)
