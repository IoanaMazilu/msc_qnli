employees_premise = 210
employees_hypothesis = 510

# the hypothesis refers to the number of employees at Veridux Corporation
if employees_hypothesis >= employees_premise:
    # check if the hypothesis value contradicts the number of employees in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of employees
    # any number of employees less than 'employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
