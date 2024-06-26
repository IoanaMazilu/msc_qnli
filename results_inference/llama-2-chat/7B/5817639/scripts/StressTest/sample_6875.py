days_worked_premise = 60
days_worked_hypothesis = 0

# the hypothesis talks about the number of days worked, which is not mentioned in the premise
if days_worked_hypothesis <= days_worked_premise:
    # check if the hypothesis value contradicts the estimate of 'days_worked_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days worked
    # any number of days worked less than 'days_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
