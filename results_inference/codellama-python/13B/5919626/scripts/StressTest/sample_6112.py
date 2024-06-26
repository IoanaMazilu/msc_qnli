employees_premise = 100
employees_hypothesis = 100

# the hypothesis talks about the number of employees in the company, referenced also in the premise
if employees_hypothesis!= employees_premise:
    # check if the hypothesis value contradicts the estimate of 'employees_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of employees
    # any number of employees greater than 'employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
