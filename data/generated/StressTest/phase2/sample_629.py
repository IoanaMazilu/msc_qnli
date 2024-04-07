# Premise: John has 10 pairs of matched socks.
# Hypothesis: John has more than 10 pairs of matched socks.
# Golden Label: contradiction

socks_premise = 10
socks_hypothesis = 10

# the hypothesis refers to the number of pairs of matched socks mentioned in the premise
if socks_hypothesis >= socks_premise:
    # check if the hypothesis value contradicts the number of pairs of matched socks in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of matched socks
    # any number of pairs of matched socks equal to 'socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

