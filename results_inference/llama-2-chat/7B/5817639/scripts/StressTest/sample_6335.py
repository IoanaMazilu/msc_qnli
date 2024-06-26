days_worked_premise = 7
days_worked_hypothesis = 8

# the hypothesis talks about the number of days worked by Ben on a task, referenced also in the premise
if days_worked_hypothesis <= days_worked_premise:
    # check if the hypothesis value contradicts the estimate of 'days_worked_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of days worked by Ben, but the hypothesis value is greater than that estimate
    # therefore, the hypothesis cannot be fully entailed from the premise, but it does not contradict it either
    label = "neutral"

print(label)
