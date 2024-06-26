employees_premise = 218
employees_hypothesis = 818

# the hypothesis talks about the number of employees in a company, referenced also in the premise
if employees_hypothesis >= employees_premise:
    # check if the hypothesis value contradicts the number of employees in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of employees
    # any number of employees less than 'employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
