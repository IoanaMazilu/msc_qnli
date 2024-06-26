nhai_employees_premise = 10
nhai_employees_hypothesis = 70

# the hypothesis refers to the number of hours worked by NHAI employees
if nhai_employees_hypothesis <= nhai_employees_premise:
    # check if the estimate of 'nhai_employees_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked
    # any number of employees greater than 'nhai_employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
