# Premise: After they have worked together for less than 32 days peter stops and Peter completes the remaining work in 10 days.
# Hypothesis: After they have worked together for 12 days peter stops and Peter completes the remaining work in 10 days.
# Golden Label: neutral

working_together_days_premise = 32
working_together_days_hypothesis = 12
remaining_work_days_premise = 10
remaining_work_days_hypothesis = 10

# the hypothesis refers to the number of days they worked together and the days Peter completed the remaining work, mentioned also in the premise

if working_together_days_hypothesis >= working_together_days_premise:
    # check if the number of 'working_together_days_hypothesis' contradicts the estimate of less than 'working_together_days_premise' in the premise
    label = "contradiction"
elif remaining_work_days_hypothesis != remaining_work_days_premise:
    # check if the number of 'remaining_work_days_hypothesis' contradicts the number of 'remaining_work_days_premise' in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days they worked together
    # any number of days less than 'working_together_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

