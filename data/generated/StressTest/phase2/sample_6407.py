# Premise: Angela has 15 pairs of matched socks.
# Hypothesis: Angela has 75 pairs of matched socks.
# Golden Label: contradiction

sock_pairs_premise = 15
sock_pairs_hypothesis = 75

# the hypothesis refers to the number of Angela's matched socks pairs mentioned in the premise
if sock_pairs_hypothesis == sock_pairs_premise:
    # check if the exact number of sock pairs in the hypothesis is the same as in the premise
    label = "entailment"
elif sock_pairs_hypothesis > sock_pairs_premise:
    # check if the number of sock pairs in the hypothesis contradicts the number of sock pairs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

