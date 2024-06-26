days_indu_premise = 1
days_indu_hypothesis = 7

# the hypothesis talks about the number of days before the work is finished, referenced also in the premise
if days_indu_hypothesis <= days_indu_premise:
    # check if the hypothesis value contradicts the estimate of more than 'days_indu_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days before the work is finished
    # any number of days before the work is finished greater than 'days_indu_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
