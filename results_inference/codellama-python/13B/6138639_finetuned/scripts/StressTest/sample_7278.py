employees_premise = 210
employees_hypothesis = 510

# the hypothesis talks about the number of employees at Veridux Corporation, referenced also in the premise
if employees_premise >= employees_hypothesis:
    # check if the number of employees in the premise contradicts the estimate of less than 'employees_hypothesis'
    label = "contradiction"
else:
    # the premise gives the exact number of employees
    # any number of employees less than 'employees_hypothesis' is consistent with the premise, and can be explicitly entailed from the premise
    label = "entailment"

print(label)
