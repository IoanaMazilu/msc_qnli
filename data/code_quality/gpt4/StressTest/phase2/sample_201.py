working_days_premise = 5
working_days_hypothesis = 8

# the hypothesis refers to the number of days they worked together mentioned in the premise
if working_days_hypothesis <= working_days_premise:
    # if 'working_days_hypothesis' is less than or equal to 'working_days_premise', we can infer entailment
    label = "entailment"
elif working_days_premise > working_days_hypothesis:
    # check if the number of working days in the premise contradicts the estimate of less than 'working_days_hypothesis' days in the hypothesis
    label = "contradiction"
else:
    # the premise gives a specific number of working days
    # any number of working days less than 'working_days_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
