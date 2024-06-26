sreedhar_work_days_premise = 75
sreedhar_work_days_hypothesis = 75

# the hypothesis talks about the number of days Sreedhar can do the work, referenced also in the premise
if sreedhar_work_days_hypothesis >= sreedhar_work_days_premise:
    # check if the hypothesis value contradicts the estimate of less than'sreedhar_work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Sreedhar can do the work
    # any number of days less than'sreedhar_work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
