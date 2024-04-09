hours_premise = 60
hours_hypothesis = 40

# the hypothesis talks about the number of hours James is paid x dollars per hour, referenced also in the premise
if hours_hypothesis > hours_premise:
    # check if the number of hours in the hypothesis contradicts the estimate of less than 'hours_premise'
    label = "contradiction"
elif hours_hypothesis < hours_premise:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
