socks_premise = 13
socks_hypothesis = 83

# the hypothesis talks about the number of socks, referenced also in the premise
if socks_hypothesis <= socks_premise:
    # check if the hypothesis value contradicts the estimate of less than'socks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of socks
    # any number of socks greater than'socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
