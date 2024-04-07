# Premise: Angela has 15 pairs of matched socks.
# Hypothesis: Angela has less than 35 pairs of matched socks.
# Golden Label: entailment

matched_socks_premise = 15
matched_socks_hypothesis = 35

# the hypothesis talks about the number of matched sock pairs Angela has, which is also referenced in the premise
if matched_socks_premise >= matched_socks_hypothesis:
    # check if the number of Angela's sock pairs in the premise contradicts the estimate of less than 'matched_socks_hypothesis'
    label = "contradiction"
elif matched_socks_premise < matched_socks_hypothesis:
    # if the premise number is less than 'matched_socks_hypothesis', it can be inferred as entailment
    label = "entailment"

print(label)

