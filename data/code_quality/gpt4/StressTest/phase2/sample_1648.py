cost_per_day_premise = 0.5
cost_per_day_hypothesis = 0.5
charged_off_time_premise = 22
charged_off_time_hypothesis = 12

# the hypothesis refers to the cost per day and the charged off time for Salley's internet provider mentioned in the premise
if cost_per_day_premise != cost_per_day_hypothesis:
    # check if the cost per day in the hypothesis contradicts the cost per day reported in the premise
    label = "contradiction"
elif charged_off_time_hypothesis >= charged_off_time_premise:
    # check if the charged off time in the hypothesis contradicts the estimate of less than 'charged_off_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the charged off time
    # any time less than 'charged_off_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
