hours_premise = 21
hours_hypothesis = 11

# the hypothesis talks about the number of hours Harry works per week, referenced also in the premise
if hours_hypothesis > hours_premise:
    # check if the hypothesis value contradicts the estimate of 'hours_premise'
    label = "contradiction"
elif hours_hypothesis < hours_premise:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
