matched_socks_premise = 70
matched_socks_hypothesis = 10

# the hypothesis talks about the number of pairs of matched socks John has, referenced also in the premise
if matched_socks_hypothesis >= matched_socks_premise:
    # check if the hypothesis value contradicts the estimate of less than'matched_socks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of matched socks
    # any number of pairs less than'matched_socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
