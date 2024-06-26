days_premise = 10
days_hypothesis = 20

# the hypothesis talks about the number of days required to complete a piece of work, referenced also in the premise
if days_hypothesis <= days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
