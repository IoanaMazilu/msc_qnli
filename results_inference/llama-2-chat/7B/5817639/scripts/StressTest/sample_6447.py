old_john_premise = 5
old_john_hypothesis = 8
old_frank_premise = 5
old_frank_hypothesis = 8

# the hypothesis talks about the age of John and Frank in less than 8 years
if old_john_hypothesis <= old_john_premise:
    # check if the hypothesis value contradicts the estimate of 'old_john_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the age of John in 5 years, and the hypothesis gives an estimate for the age of John in less than 8 years
    # any age of John greater than 'old_john_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
