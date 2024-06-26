days_work_premise = 60
days_work_hypothesis = 40

# the hypothesis talks about the number of days Jhon works, referenced also in the premise
if days_work_premise >= days_work_hypothesis:
    # check if the estimate of 'days_work_hypothesis' contradicts the number of days Jhon works in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'days_work_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
