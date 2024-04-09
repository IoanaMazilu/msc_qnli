employees_premise = 210
employees_hypothesis = 510

# the hypothesis refers to the number of employees at Veridux Corporation
if employees_hypothesis <= employees_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif employees_hypothesis < employees_premise:
    # check if the hypothesis value is less than the premise value
    label = "entailment"
else:
    # the premise gives only an estimate for the number of employees
    # any number of employees less than 510 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
