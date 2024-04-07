# Premise: Mary can do a piece of work in less than 38 days.
# Hypothesis: Mary can do a piece of work in 28 days.
# Golden Label: neutral

work_days_premise = 38
work_days_hypothesis = 28

# the hypothesis refers to the number of days Mary needs to finish a piece of work, also mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days less than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

