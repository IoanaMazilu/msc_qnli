employees_premise = 210
employees_hypothesis = 200

# the hypothesis refers to the number of employees at Veridux Corporation
if employees_premise > employees_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif employees_hypothesis == employees_premise:
    # check if the hypothesis value is consistent with the premise value
    label = "neutral"
else:
    # the premise value is an estimate, and the hypothesis value is less than the estimate
    # any number of employees less than 210 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
