sreedhar_work_days_premise = 25
sreedhar_work_days_hypothesis = 75

# the hypothesis refers to the number of days Sreedhar can do the work, which is also mentioned in the premise
if sreedhar_work_days_hypothesis <= sreedhar_work_days_premise:
    # check if the hypothesis value contradicts the estimate of more than'sreedhar_work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Sreedhar can do the work
    # any number of days greater than'sreedhar_work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
