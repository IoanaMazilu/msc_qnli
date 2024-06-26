alone_work_days_premise = 15
alone_work_days_hypothesis = 15
joint_work_days = 3

# the hypothesis refers to the number of days he worked alone before being joined by Kennedy, which is also mentioned in the premise
if alone_work_days_hypothesis >= alone_work_days_premise:
    # check if the hypothesis value contradicts the premise of him working alone for less than 'alone_work_days_premise' days
    label = "contradiction"
else:
    # the premise gives the exact number of days he worked alone
    # any number of days less than 'alone_work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
