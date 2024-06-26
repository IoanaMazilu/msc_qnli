days_work_premise = 5
days_work_hypothesis = 5

# the hypothesis talks about the number of days they work together, referenced also in the premise
if days_work_hypothesis <= days_work_premise:
    # check if the hypothesis value contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'days_work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
