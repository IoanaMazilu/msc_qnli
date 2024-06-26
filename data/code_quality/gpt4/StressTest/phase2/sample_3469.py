work_days_premise = 30
work_days_hypothesis = 20

# The hypothesis refers to the number of days Sakshi can do a piece of work, which is also referenced in the premise
if work_days_hypothesis >= work_days_premise:
    # Check if the hypothesis value contradicts the premise that Sakshi can do the work in less than 'work_days_premise' days
    label = "contradiction"
else:
    # The premise gives an estimate for the number of days Sakshi can do the work
    # Any number of days less than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
