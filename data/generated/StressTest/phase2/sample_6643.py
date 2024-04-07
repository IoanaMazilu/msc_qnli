# Premise: Marcella has more than 17 pairs of shoes.
# Hypothesis: Marcella has 27 pairs of shoes.
# Golden Label: neutral

pairs_shoes_premise = 17
pairs_shoes_hypothesis = 27

# the hypothesis talks about the number of pairs of shoes Marcella has, referenced also in the premise
if pairs_shoes_hypothesis <= pairs_shoes_premise:
    # check if the hypothesis value contradicts the estimate of more than 'pairs_shoes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of shoes
    # any number of pairs greater than 'pairs_shoes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

