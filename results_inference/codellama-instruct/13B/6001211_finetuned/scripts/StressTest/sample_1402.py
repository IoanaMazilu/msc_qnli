work_days_sreedhar_premise = 25
work_days_sreedhar_hypothesis = 75

# the hypothesis refers to the number of days Sreedhar can do the work alone, mentioned also in the premise
if work_days_sreedhar_hypothesis <= work_days_sreedhar_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_days_sreedhar_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'work_days_sreedhar_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)