months_later_premise = 8
months_later_hypothesis = 2

# the hypothesis talks about the time when Jose joined him, also referenced in the premise
if months_later_hypothesis >= months_later_premise:
    # check if the hypothesis estimate contradicts the number of months in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of months
    # any number of months consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
