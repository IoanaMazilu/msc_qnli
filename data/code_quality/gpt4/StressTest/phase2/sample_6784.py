regular_hours_premise = 70
regular_hours_hypothesis = 40

# the hypothesis refers to the number of regular hours worked by James each week, also mentioned in the premise
if regular_hours_hypothesis >= regular_hours_premise:
    # check if the number of regular hours in the hypothesis contradicts the estimate of less than 'regular_hours_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of regular hours
    # a number of regular hours less than 'regular_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
