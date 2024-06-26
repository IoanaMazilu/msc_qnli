days_work_premise = 5
days_work_hypothesis = 3

# the hypothesis talks about the number of days worked by both people
if days_work_hypothesis <= days_work_premise:
    # check if the hypothesis value contradicts the estimate of more than 'days_work_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days worked
    # any number of days greater than 'days_work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
