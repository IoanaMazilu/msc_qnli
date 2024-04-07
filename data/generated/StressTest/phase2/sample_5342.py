# Premise: Mary works in a restaurant a maximum of 80 hours.
# Hypothesis: Mary works in a restaurant a maximum of 10 hours.
# Golden Label: contradiction

work_hours_premise = 80
work_hours_hypothesis = 10

# the hypothesis refers to the maximum number of hours Mary works in the restaurant mentioned in the premise
if work_hours_hypothesis > work_hours_premise:
    # check if the maximum working hours in the hypothesis contradicts the maximum number of working hours in the premise
    label = "contradiction"
elif work_hours_hypothesis == work_hours_premise:
    # if the maximum number of working hours in the hypothesis is the same as the premise, we can infer entailment
    label = "entailment"
else:
    # any number of working hours less than 'work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

