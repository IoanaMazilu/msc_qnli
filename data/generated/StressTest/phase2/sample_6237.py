# Premise: John has 10 pairs of matched socks.
# Hypothesis: John has less than 40 pairs of matched socks.
# Golden Label: entailment

pairs_of_socks_premise = 10
pairs_of_socks_hypothesis = 40

# the hypothesis refers to the number of matched socks John has, mentioned in the premise as well
if pairs_of_socks_hypothesis <= pairs_of_socks_premise:
    # if 'pairs_of_socks_hypothesis' is less than or equal to 'pairs_of_socks_premise'
    # then the hypothesis contradicts the premise
    label = "contradiction"
elif pairs_of_socks_premise < pairs_of_socks_hypothesis:
    # if 'pairs_of_socks_premise' is less than 'pairs_of_socks_hypothesis'
    # then the premise fully and explicitly entails the hypothesis
    label = "entailment"

print(label)

