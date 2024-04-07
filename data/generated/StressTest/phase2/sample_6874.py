# Premise: Jhon works for more than 40 days.
# Hypothesis: Jhon works for 60 days.
# Golden Label: neutral

work_days_premise = 40
work_days_hypothesis = 60

# the hypothesis refers to the number of work days mentioned in the premise
if work_days_hypothesis <= work_days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of work days
    # any number of work days greater than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

