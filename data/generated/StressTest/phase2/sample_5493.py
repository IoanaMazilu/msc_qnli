# Premise: If he worked for 15 days alone before he was joined by Kennedy to complete the job in 3 days, how many days will it take both of them to complete the entire job?
# Hypothesis: If he worked for less than 55 days alone before he was joined by Kennedy to complete the job in 3 days, how many days will it take both of them to complete the entire job?
# Golden Label: entailment

work_days_alone_premise = 15
work_days_alone_hypothesis = 55
work_days_together = 3

# the hypothesis refers to the number of days he worked alone, also mentioned in the premise
if work_days_alone_premise >= work_days_alone_hypothesis:
    # check if the premise value contradicts the estimate of less than 'work_days_alone_hypothesis'
    label = "contradiction"
else:
    # the hypothesis gives only an estimate for the number of days he worked alone
    # any number of days less than 'work_days_alone_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

