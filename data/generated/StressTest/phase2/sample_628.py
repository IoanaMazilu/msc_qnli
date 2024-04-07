# Premise: John has less than 70 pairs of matched socks.
# Hypothesis: John has 10 pairs of matched socks.
# Golden Label: neutral

socks_premise = 70
socks_hypothesis = 10

# the hypothesis talks about the number of socks John has, referenced also in the premise
if socks_hypothesis >= socks_premise:
    # check if the hypothesis value contradicts the premise of less than 'socks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of socks
    # any number of socks less than 'socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

