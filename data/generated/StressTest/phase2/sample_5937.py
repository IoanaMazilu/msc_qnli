# Premise: At Veridux Corporation, there are 180 employees.
# Hypothesis: At Veridux Corporation, there are less than 280 employees.
# Golden Label: entailment

employees_premise = 180
employees_hypothesis = 280

# the hypothesis refers to the number of employees in the Veridux Corporation
if employees_hypothesis <= employees_premise:
    # check if the hypothesis estimate contradicts the number of employees stated in the premise
    label = "contradiction"
elif employees_premise != employees_hypothesis:
    # check if the number of employees in the hypothesis contradicts the number of employees stated in the premise
    label = "entailment"
else:
    # the premise gives the exact number of employees
    # any number of employees less than 'employees_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

