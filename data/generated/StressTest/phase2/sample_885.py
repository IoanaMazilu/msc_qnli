# Premise: Mary works in a restaurant a maximum of 45 hours.
# Hypothesis: Mary works in a restaurant a maximum of more than 15 hours.
# Golden Label: entailment

work_hours_premise = 45
work_hours_hypothesis = 15

# the hypothesis refers to the maximum number of work hours in the premise
if work_hours_premise < work_hours_hypothesis:
    # check if the estimate of 'work_hours_hypothesis' contradicts the number of work hours in the premise
    label = "contradiction"
elif work_hours_hypothesis > work_hours_premise:
    # check if the number of work hours in the hypothesis contradicts the maximum number of work hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

