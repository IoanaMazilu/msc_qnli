employees_premise = less_than_280
employees_hypothesis = 180

# the hypothesis refers to the number of employees at Veridux Corporation
if employees_hypothesis <= employees_premise:
    # check if the hypothesis value contradicts the estimate of less than 'employees_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of employees
    # any number of employees less than or equal to 180 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
