# Premise: At Veridux Corporation, there are less than 300 employees.
# Hypothesis: At Veridux Corporation, there are 200 employees.
# Golden Label: neutral

employees_premise = 300
employees_hypothesis = 200

# the hypothesis talks about the number of employees in Veridux Corporation, referenced also in the premise
if employees_hypothesis >= employees_premise:
    # check if the hypothesis value contradicts the estimate of less than 'employees_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of employees
    # any number of employees less than 'employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

