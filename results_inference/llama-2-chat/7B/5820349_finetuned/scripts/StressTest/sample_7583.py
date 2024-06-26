work_days_sreedhar_premise = 75
work_days_sreedhar_hypothesis = 75

# the hypothesis refers to the number of days Sreedhar can do the work, which is also mentioned in the premise
if work_days_sreedhar_hypothesis >= work_days_sreedhar_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
