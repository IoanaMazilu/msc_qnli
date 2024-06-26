working_days_premise = 3
working_days_hypothesis = 5

# the hypothesis talks about the number of days they both work together, referenced also in the premise
if working_days_hypothesis <= working_days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'working_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of working days
    # any number of working days greater than 'working_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
