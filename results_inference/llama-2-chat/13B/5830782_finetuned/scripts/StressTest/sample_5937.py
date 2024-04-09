employees_premise = 180
employees_hypothesis = 280

# the hypothesis refers to the number of employees at Veridux Corporation mentioned in the premise
if employees_premise >= employees_hypothesis:
    # check if the number of employees in the premise contradicts the estimate of less than 'employees_hypothesis'
    label = "contradiction"
else:
    # if the number of employees in the premise does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
