socks_premise = 6
socks_hypothesis = 2

# the hypothesis refers to the number of socks Barbara wears, mentioned also in the premise
if socks_hypothesis >= socks_premise:
    # check if the number of socks Barbara wears in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives a minimum number of socks Barbara can wear
    # any number of socks less than'socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
