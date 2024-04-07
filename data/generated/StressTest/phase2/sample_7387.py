# Premise: Mary can do a piece of work in less than 81 days.
# Hypothesis: Mary can do a piece of work in 11 days.
# Golden Label: neutral

work_days_premise = 81
work_days_hypothesis = 11

# the hypothesis refers to the number of days Mary can finish a piece of work, which is also mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days less than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

