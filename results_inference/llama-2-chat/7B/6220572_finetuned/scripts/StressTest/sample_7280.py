employees_premise = 210
employees_hypothesis = 210

# the hypothesis talks about the number of employees at Veridux Corporation, referenced also in the premise
if employees_hypothesis >= employees_premise:
    # check if the hypothesis value contradicts the number of employees reported in the premise
    label = "contradiction"
else:
    # the premise gives a specific number of employees
    # any number of employees less than 'employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
