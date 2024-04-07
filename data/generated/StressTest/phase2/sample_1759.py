# Premise: After they have worked together for less than 82 days Matt stops and Peter completes the remaining work in 10 days.
# Hypothesis: After they have worked together for 12 days Matt stops and Peter completes the remaining work in 10 days.
# Golden Label: neutral

work_days_together_premise = 82
work_days_together_hypothesis = 12
remaining_work_days_peter_premise = 10
remaining_work_days_peter_hypothesis = 10

# the hypothesis refers to the days worked together by Matt and Peter and the remaining days Peter worked alone 
if work_days_together_hypothesis >= work_days_together_premise:
    # check if the number of days worked together in the hypothesis contradicts the estimate of less than 'work_days_together_premise' days
    label = "contradiction"
elif remaining_work_days_peter_hypothesis != remaining_work_days_peter_premise:
    # check if the remaining work days in the hypothesis contradicts the remaining work days reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days worked together
    # any number of days less than 'work_days_together_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

