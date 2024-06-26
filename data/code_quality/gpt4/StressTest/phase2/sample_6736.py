work_days_rohit_premise = 22
work_days_rohan_premise = 6
work_days_rohit_hypothesis = 12
work_days_rohan_hypothesis = 6

# the hypothesis talks about the number of days Rohit and Rohan need to complete a work, referenced also in the premise
if work_days_rohit_hypothesis >= work_days_rohit_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_days_rohit_premise'
    label = "contradiction"
elif work_days_rohan_hypothesis != work_days_rohan_premise:
    # check if the hypothesis value contradicts the 'work_days_rohan_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Rohit needs
    # any number of days less than 'work_days_rohit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
