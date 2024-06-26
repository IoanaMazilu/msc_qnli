white_socks_premise = 50
white_socks_hypothesis = 40

# the hypothesis talks about the percentage of white socks in a shop, also referenced in the premise
if white_socks_hypothesis >= white_socks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'white_socks_premise'
    label = "contradiction"
elif white_socks_hypothesis < white_socks_premise:
    # check if the hypothesis value can be explicitly derived from the estimate of less than 'white_socks_premise'
    label = "entailment"
else:
    # the premise gives only an estimate for the percentage of white socks
    # any percentage of white socks less than 'white_socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
