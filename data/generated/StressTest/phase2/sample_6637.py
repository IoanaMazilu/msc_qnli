# Premise: Ram, Krish and Bhim can complete a work in less than 50 days.
# Hypothesis: Ram, Krish and Bhim can complete a work in 30 days.
# Golden Label: neutral

work_days_premise = 50
work_days_hypothesis = 30

# the hypothesis refers to the number of days for Ram, Krish and Bhim to complete a work mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days less than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

