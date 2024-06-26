hours_premise = 40
hours_hypothesis = 70
# the hypothesis talks about the number of hours James is paid x dollars for, referenced also in the premise
if hours_hypothesis > hours_premise:
    # check if the hypothesis value contradicts the estimate of 'hours_premise'
    label = "contradiction"
elif hours_hypothesis < hours_premise:
    # the premise gives a definite number of hours James is paid x dollars for
    # if the number of hours in the hypothesis is less than 'hours_premise', it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the number of hours in the hypothesis equals 'hours_premise', we can infer entailment
    label = "entailment"

print(label)
