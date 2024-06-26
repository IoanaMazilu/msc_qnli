socks_premise = 70
socks_hypothesis = 10

# the hypothesis refers to the number of pairs of matched socks mentioned in the premise
if socks_hypothesis <= socks_premise:
    # check if the hypothesis value contradicts the number of pairs of socks in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of socks
    # any number of pairs of socks greater than'socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
