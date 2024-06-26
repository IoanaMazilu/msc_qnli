work_hours_premise = 60
work_hours_hypothesis = 10

# the hypothesis refers to the maximum number of work hours of Mary, also mentioned in the premise
if work_hours_premise < work_hours_hypothesis:
    # check if the maximum number of work hours in the premise contradicts the 'work_hours_hypothesis'
    label = "contradiction"
elif work_hours_premise == work_hours_hypothesis:
    # check if the max work hours in the premise equal the 'work_hours_hypothesis'
    label = "contradiction"
else:
    # the premise gives a maximum limit for the work hours
    # any maximum work hours more than 'work_hours_hypothesis' is consistent with the premise, but cannot be explicitly entailed
    label = "neutral"

print(label)
