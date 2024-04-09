angela_socks_premise = 13
angela_socks_hypothesis = 83

# the hypothesis refers to the number of pairs of socks owned by Angela
if angela_socks_hypothesis <= angela_socks_premise:
    # check if the hypothesis value contradicts the estimate of 'angela_socks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of socks
    # any number of pairs of socks less than 'angela_socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
