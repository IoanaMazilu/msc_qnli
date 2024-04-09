angela_socks_premise = 13
angela_socks_hypothesis = 83

# the hypothesis talks about the number of pairs of socks owned by Angela
if angela_socks_hypothesis <= angela_socks_premise:
    # check if the hypothesis value contradicts the estimate of 13 pairs
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of socks
    # any number of pairs greater than 13 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
