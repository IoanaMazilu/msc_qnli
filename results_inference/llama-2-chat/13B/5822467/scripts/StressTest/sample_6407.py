angela_socks_premise = 15
angela_socks_hypothesis = 75

# the hypothesis talks about the number of pairs of socks Angela has, referenced also in the premise
if angela_socks_hypothesis <= angela_socks_premise:
    # check if the hypothesis value contradicts the estimate of 15 pairs in the premise
    label = "contradiction"
elif angela_socks_hypothesis > angela_socks_premise:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # the premise gives only an estimate for the number of pairs of socks Angela has
    # any number of pairs greater than 15 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
