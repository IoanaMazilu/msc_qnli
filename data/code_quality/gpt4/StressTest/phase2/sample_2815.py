employees_premise = 815
employees_hypothesis = 215

# the hypothesis refers to the number of employees at Veridux Corporation, mentioned also in the premise
if employees_hypothesis >= employees_premise:
    # check if the number of employees in the hypothesis contradicts the estimate of less than 'employees_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of employees
    # any number of employees less than 'employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
