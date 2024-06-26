employees_veridux_premise = 550
employees_veridux_hypothesis = 250

# the hypothesis talks about the number of employees at Veridux Corporation, referenced also in the premise
if employees_veridux_hypothesis >= employees_veridux_premise:
    # check if the hypothesis value contradicts the estimate of less than 'employees_veridux_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of employees
    # any number of employees less than 'employees_veridux_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
