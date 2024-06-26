days_worked_premise = 12
days_worked_hypothesis = 72

# the hypothesis talks about the number of days worked by Matt and Peter, referenced also in the premise
if days_worked_hypothesis <= days_worked_premise:
    # check if the hypothesis value contradicts the estimate of 'days_worked_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of days worked by Matt and Peter
    # any number of days greater than 'days_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
