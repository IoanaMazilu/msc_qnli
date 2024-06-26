matched_socks_premise = 14
matched_socks_hypothesis = 34

# the hypothesis talks about the number of matched socks Angela has, referenced also in the premise
if matched_socks_premise >= matched_socks_hypothesis:
    # check if the premise value contradicts the estimate of less than 'matched_socks_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact count for the number of matched socks
    # any number of socks less than 'matched_socks_hypothesis' is consistent with the premise, and can be explicitly entailed from the premise if the number is 14
    label = "entailment"

print(label)
