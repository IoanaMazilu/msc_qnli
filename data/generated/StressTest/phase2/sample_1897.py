# Premise: Matt and Peter can do together a piece of work in more than 10 days.
# Hypothesis: Matt and Peter can do together a piece of work in 20 days.
# Golden Label: neutral

work_days_premise = 10
work_days_hypothesis = 20

# the hypothesis refers to the number of days required for Matt and Peter to complete a work, mentioned also in the premise
if work_days_hypothesis <= work_days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
