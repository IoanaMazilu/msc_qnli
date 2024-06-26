average_premise = 60
average_hypothesis = 60

# the hypothesis talks about the average test score of Joe, which is also referred to in the premise
if average_hypothesis == average_premise:
    # the hypothesis and premise values are the same, so entailment
    label = "entailment"
elif average_hypothesis > average_premise:
    # the hypothesis value is greater than the premise value, so contradiction
    label = "contradiction"
else:
    # the premise gives only an estimate for the average test score, so any value greater than that is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
