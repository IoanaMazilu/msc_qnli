specific_socks_premise = 6
specific_socks_hypothesis = 2

# the hypothesis refers to the number of specific socks Barbara wears, also mentioned in the premise
if specific_socks_hypothesis <= specific_socks_premise:
    # check if the hypothesis value contradicts the number of specific socks in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of specific socks
    # any number of specific socks greater than'specific_socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
