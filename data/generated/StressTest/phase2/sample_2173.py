# Premise: John has less than 60 pairs of matched socks.
# Hypothesis: John has 10 pairs of matched socks.
# Golden Label: neutral

matched_socks_premise = 60
matched_socks_hypothesis = 10

# the hypothesis refers to the number of John's matched socks mentioned in the premise
if matched_socks_hypothesis >= matched_socks_premise:
    # check if the number of 'matched_socks_hypothesis' contradicts the number of matched socks in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of matched socks
    # any number of matched socks less than 'matched_socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

