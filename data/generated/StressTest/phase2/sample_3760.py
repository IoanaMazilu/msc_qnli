# Premise: Mary can do a piece of work in less than 72 days.
# Hypothesis: Mary can do a piece of work in 12 days.
# Golden Label: neutral

work_days_premise = 72
work_days_hypothesis = 12

# The hypothesis refers to the number of days Mary can do a piece of work, which is also mentioned in the premise.
if work_days_hypothesis >= work_days_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'work_days_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of days
    # Any number of days less than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

