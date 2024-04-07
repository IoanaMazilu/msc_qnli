# Premise: John has 10 pairs of matched socks.
# Hypothesis: John has 20 pairs of matched socks.
# Golden Label: contradiction

matched_socks_premise = 10
matched_socks_hypothesis = 20

# the hypothesis refers to the number of matched socks pairs that John has, also mentioned in the premise
if matched_socks_hypothesis == matched_socks_premise:
    # check if the number in the hypothesis directly matches the one from the premise
    label = "entailment"
elif matched_socks_hypothesis < matched_socks_premise:
    # check if the number in the hypothesis contradicts the one from the premise
    label = "contradiction"
else:
    # the hypothesis suggests a number of matched socks pairs greater than the one in the premise,
    # which does not contradict the premise but cannot be explicitly entailed from it
    label = "neutral"

print(label)

