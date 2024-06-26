employees_premise = 210
employees_hypothesis = 210

# the hypothesis refers to the number of employees at Veridux Corporation, mentioned in the premise
if employees_hypothesis >= employees_premise:
    # check if the estimate of 'employees_hypothesis' contradicts the number of employees in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of employees
    # any number of employees less than 'employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)