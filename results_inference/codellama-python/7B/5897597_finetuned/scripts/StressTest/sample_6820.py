socks_premise = 6
socks_hypothesis = 2

# the hypothesis refers to the number of socks Barbara doesn't wear, which is also mentioned in the premise
if socks_hypothesis >= socks_premise:
    # check if the hypothesis value contradicts the estimate of'socks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of socks
    # any number of socks less than'socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
