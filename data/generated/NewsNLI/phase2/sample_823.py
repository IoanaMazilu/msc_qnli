# Premise: Two of the Spanish nationals arrested were living aboard the yacht and another two were arrested after they were discovered allegedly meeting the yacht in the northeastern coastal town of Bundaberg.
# Hypothesis: Four Spanish nationals were arrested in connection with the cocaine seizure.
# Golden Label: neutral

spanish_nationals_premise = 2 + 2
spanish_nationals_hypothesis = 4

# the hypothesis mentions the number of Spanish nationals arrested, which is also referenced in the premise
# the hypothesis does not specify where they were arrested or for what specific reason
if spanish_nationals_hypothesis == spanish_nationals_premise:
    # check if the number of Spanish nationals in the hypothesis matches the number in the premise
    label = "entailment"
else:
    # if the numbers do not match, it's a contradiction
    label = "contradiction"

print(label)

