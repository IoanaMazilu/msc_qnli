well_digging_days_premise = 7
well_digging_days_hypothesis = 8

# the hypothesis talks about the number of days needed for Jake, Paul and Hari to dig a well, which is also referenced in the premise
if well_digging_days_hypothesis <= well_digging_days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'well_digging_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'well_digging_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
