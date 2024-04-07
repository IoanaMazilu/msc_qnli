# Premise: John has 10 pairs of matched socks.
# Hypothesis: John has 60 pairs of matched socks.
# Golden Label: contradiction

socks_premise = 10
socks_hypothesis = 60

# the hypothesis refers to the number of pairs of matched socks that John has, which is also mentioned in the premise
if socks_hypothesis != socks_premise:
    # check if the number of pairs of socks in the hypothesis contradicts the number of pairs of socks reported in the premise
    label = "contradiction"
else:
    # the premise and hypothesis values are identical, hence entailment
    label = "entailment"

print(label)

