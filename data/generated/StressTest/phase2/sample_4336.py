# Premise: At Veridux Corporation, there are less than 850 employees.
# Hypothesis: At Veridux Corporation, there are 250 employees.
# Golden Label: neutral

employees_premise = 850
employees_hypothesis = 250

# the hypothesis states a specific number of employees at Veridux Corporation, which is also referenced in the premise
if employees_hypothesis >= employees_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'employees_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of employees
    # any number of employees less than 'employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

