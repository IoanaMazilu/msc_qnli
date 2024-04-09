less_than_70_premise = 70
less_than_70_hypothesis = 10

# the hypothesis talks about the number of pairs of matched socks owned by John
if less_than_70_hypothesis <= less_than_70_premise:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_70_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of matched socks
    # any number of pairs of matched socks greater than 'less_than_70_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
