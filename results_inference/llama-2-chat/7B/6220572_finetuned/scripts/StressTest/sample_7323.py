increase_week_premise = 1
increase_week_hypothesis = 2

# the hypothesis talks about the increase in the number of gym visits per week, also referenced in the premise
if increase_week_hypothesis <= increase_week_premise:
    # check if the hypothesis value contradicts the increase in 'increase_week_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the increase in 'increase_week_premise'
    # any increase greater than 'increase_week_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
