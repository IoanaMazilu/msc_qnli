regular_hours_premise = 18
regular_hours_hypothesis = 68
overtime_rate = 1.5

# the hypothesis refers to the number of regular hours and overtime rate mentioned in the premise
if regular_hours_hypothesis > regular_hours_premise:
    # check if the number of regular hours in the hypothesis contradicts the number of regular hours reported in the premise
    label = "contradiction"
elif regular_hours_hypothesis < regular_hours_premise:
    # the premise gives an exact number for the regular hours
    # any number of regular hours less than 'regular_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
