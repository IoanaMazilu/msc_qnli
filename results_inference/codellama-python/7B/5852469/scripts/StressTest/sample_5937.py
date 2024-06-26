employees_premise = 180
employees_hypothesis = 280

# the hypothesis refers to the number of employees in the premise
if employees_hypothesis <= employees_premise:
    # check if the estimate of 'employees_hypothesis' contradicts the number of employees in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of employees
    # any number of employees greater than 'employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
