# Premise: John has 10 pairs of matched socks.
# Hypothesis: John has less than 60 pairs of matched socks.
# Golden Label: entailment

matched_socks_premise = 10
matched_socks_hypothesis = 60

# The hypothesis talks about the number of matched socks John has, which is also mentioned in the premise
if matched_socks_premise >= matched_socks_hypothesis:
    # Check if the number of socks in the premise contradicts the 'less than matched_socks_hypothesis' statement
    label = "contradiction"
elif matched_socks_premise == matched_socks_hypothesis:
    # The premise exactly matches the number of socks stated in the hypothesis
    label = "entailment"
else:
    # The premise gives an exact number of socks, any number greater than 'matched_socks_premise' and less than 'matched_socks_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

