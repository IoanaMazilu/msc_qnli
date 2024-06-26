# the hypothesis talks about the time when Jose joined him, referenced also in the premise
if hypothesis.months < 8:
    # check if the estimate of 'hypothesis.months' contradicts the number of months in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of months
    # any number of months less than 'hypothesis.months' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
