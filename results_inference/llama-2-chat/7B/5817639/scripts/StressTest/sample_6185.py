employees_premise = 218
employees_hypothesis = 118

# the hypothesis talks about the number of employees at Veridux Corporation, referenced also in the premise
if employees_hypothesis <= employees_premise:
    # check if the hypothesis value contradicts the estimate of more than 'employees_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of employees
    # any number of employees greater than 'employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
