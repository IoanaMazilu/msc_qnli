old_john_premise = 3 * 6 = 18
old_john_hypothesis = 3 * (5 + 1) = 21

# the hypothesis talks about John's age more than 5 years back, referenced also in the premise
if old_john_hypothesis <= old_john_premise:
    # check if the hypothesis value contradicts the estimate of John's age in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for John's age more than 5 years back
    # any age greater than 'old_john_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
