employees_premise = 218
employees_hypothesis = 818

# the hypothesis talks about the number of employees at Veridux Corporation, referenced also in the premise
if employees_premise >= employees_hypothesis:
    # check if the number of employees in the premise contradicts the estimate of less than 'employees_hypothesis'
    label = "contradiction"
else:
    # the premise gives the exact number of employees
    # any number of employees less than 'employees_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
