# Premise: At Veridux Corporation, there are less than 280 employees.
# Hypothesis: At Veridux Corporation, there are 180 employees.
# Golden Label: neutral

employees_premise = 280
employees_hypothesis = 180

# the hypothesis gives a specific number of employees at Veridux Corporation mentioned in the premise
if employees_hypothesis >= employees_premise:
    # check if the hypothesis value contradicts the estimate of less than 'employees_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of employees
    # any number of employees less than 'employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

