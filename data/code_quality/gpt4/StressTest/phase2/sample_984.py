socks_premise = 12
socks_hypothesis = 72

# the hypothesis talks about the number of socks Angela has, referenced also in the premise
if socks_premise >= socks_hypothesis:
    # check if the hypothesis value contradicts the exact number of 'socks_premise'
    label = "contradiction"
else:
    # the premise gives an exact number for the socks
    # any number of socks less than 'socks_hypothesis' is consistent with the premise, and can be explicitly entailed from the premise
    label = "entailment"

print(label)
