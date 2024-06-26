work_days_premise = 25
work_days_hypothesis = 25

# the hypothesis refers to the number of days Sreedhar and Sravan can do a work, mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives the exact number of days
    # any number of days less than 'work_days_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
