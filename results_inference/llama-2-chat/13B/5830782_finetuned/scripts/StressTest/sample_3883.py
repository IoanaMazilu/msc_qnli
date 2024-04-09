total_hours_premise = 4
total_hours_hypothesis = 3

# the hypothesis refers to the total hours Aaron spends jogging and walking, which is also mentioned in the premise
if total_hours_hypothesis >= total_hours_premise:
    # check if the total hours in the hypothesis contradicts the estimate of less than 'total_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total hours
    # any number of hours less than 'total_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
