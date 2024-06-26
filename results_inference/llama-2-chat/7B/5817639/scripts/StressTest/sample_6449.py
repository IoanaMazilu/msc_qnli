old_john_premise = 5
old_john_hypothesis = 7
old_frank_premise = 5
old_frank_hypothesis = 5

# the hypothesis talks about the age of John and Frank in 7 years, referenced also in the premise
if old_john_hypothesis <= old_john_premise:
    # check if the hypothesis value contradicts the estimate of John's age in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for John's age in 5 years
    # any age of John greater than 'old_john_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
