# Premise: Angela has 13 pairs of matched socks.
# Hypothesis: Angela has 83 pairs of matched socks.
# Golden Label: contradiction

matched_socks_premise = 13
matched_socks_hypothesis = 83

# the hypothesis talks about the number of Angela's matched socks, referenced also in the premise
if matched_socks_hypothesis == matched_socks_premise:
    # check if the number of matched socks in the hypothesis is the same as in the premise
    label = "entailment"
elif matched_socks_hypothesis < matched_socks_premise:
    # check if the number of matched socks in the hypothesis contradicts the number of matched socks in the premise
    label = "contradiction"
else:
    # the number of matched socks in the hypothesis is greater than in the premise,
    # so it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "contradiction"

print(label)

