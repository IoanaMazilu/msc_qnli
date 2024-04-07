# Premise: After they have worked together for less than 30 days Matt stops and Peter completes the remaining work in 10 days.
# Hypothesis: After they have worked together for 10 days Matt stops and Peter completes the remaining work in 10 days.
# Golden Label: neutral

total_working_days_premise = 30
total_working_days_hypothesis = 10
remaining_days_peter_works = 10

# the hypothesis refers to the duration Matt and Peter worked together and the remaining days Peter worked alone
if total_working_days_hypothesis >= total_working_days_premise:
    # check if the duration of working together in the hypothesis contradicts the estimate of less than 'total_working_days_premise'
    label = "contradiction"
elif remaining_days_peter_works != remaining_days_peter_works:
    # check if the remaining days Peter worked alone in the hypothesis contradicts the same number of days reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total working days together
    # any number of days less than 'total_working_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

