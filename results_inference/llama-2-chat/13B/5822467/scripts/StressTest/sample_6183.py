employees_premise = 218
employees_hypothesis = 818

# the hypothesis refers to the number of employees at Veridux Corporation
if employees_hypothesis <= employees_premise:
    # check if the hypothesis value contradicts the estimate of 'employees_premise'
    label = "contradiction"
elif employees_hypothesis < employees_premise:
    # the hypothesis value is less than the premise estimate, but the difference is not large enough to contradict
    label = "neutral"
else:
    # the premise gives only an estimate for the number of employees
    # any number of employees less than 'employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
