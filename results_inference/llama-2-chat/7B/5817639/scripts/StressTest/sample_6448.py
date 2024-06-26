old_john_premise = 8
old_john_hypothesis = 5

# the hypothesis talks about John's age in a specific time frame, referenced also in the premise
if old_john_hypothesis <= old_john_premise:
    # check if the hypothesis value contradicts the estimate of John's age in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for John's age in the future, which cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
