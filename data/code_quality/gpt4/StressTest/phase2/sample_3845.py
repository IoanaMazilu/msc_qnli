employees_premise = 200
employees_hypothesis = 200

# the hypothesis talks about the number of employees in Veridux Corporation, which is also referenced in the premise
if employees_hypothesis != employees_premise:
    # check if the hypothesis value contradicts the exact number of employees in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of employees
    # the same number of employees in the hypothesis is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)
