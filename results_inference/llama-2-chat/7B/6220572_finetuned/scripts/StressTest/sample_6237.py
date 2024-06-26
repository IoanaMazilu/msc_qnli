socks_premise = 10
socks_hypothesis = 40

# the hypothesis refers to the number of socks John has, also mentioned in the premise
if socks_hypothesis >= socks_premise:
    # check if the hypothesis value contradicts the number of socks reported in the premise
    label = "contradiction"
else:
    # any number of socks less than'socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
