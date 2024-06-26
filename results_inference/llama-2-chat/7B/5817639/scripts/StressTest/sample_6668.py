work_days_premise = 20
work_days_hypothesis = 50

# the hypothesis talks about the number of days Kamal will take to complete work, which is also mentioned in the premise
if work_days_hypothesis <= work_days_premise:
    # check if the hypothesis value contradicts the estimate of 'work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Kamal will take to complete work
    # any number of days greater than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
