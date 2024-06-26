ys_premise = 35
ys_hypothesis = 15

# the hypothesis talks about the number of pairs of matched socks Angela has, referenced also in the premise
if ys_hypothesis >= ys_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ys_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of matched socks
    # any number of pairs less than 'ys_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
