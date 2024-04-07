# Premise: They both work together for more than 1 days and then Sushil goes away.
# Hypothesis: They both work together for 5 days and then Sushil goes away.
# Golden Label: neutral

work_days_premise = 1
work_days_hypothesis = 5

# the hypothesis refers to the number of days they worked together, also mentioned in the premise
if work_days_hypothesis <= work_days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

