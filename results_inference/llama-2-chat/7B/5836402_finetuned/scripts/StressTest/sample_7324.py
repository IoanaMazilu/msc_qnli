increase_week_premise = 2
increase_week_hypothesis = 1

# the hypothesis refers to the number of weeks it takes for the average number of gym visits to increase, which is also mentioned in the premise
if increase_week_hypothesis >= increase_week_premise:
    # check if the hypothesis value contradicts the estimate of less than 'increase_week_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks
    # any number of weeks less than 'increase_week_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
