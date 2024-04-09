socks_premise = 10
socks_hypothesis = 20

# check if the hypothesis value contradicts the estimate of'socks_premise'
if socks_hypothesis > socks_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of socks
    # any number of socks greater than'socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
