# Premise: Marcella has more than 16 pairs of shoes.
# Hypothesis: Marcella has 26 pairs of shoes.
# Golden Label: neutral

shoes_premise = 16
shoes_hypothesis = 26

# the hypothesis talks about the number of shoes Marcella has, which is also mentioned in the premise
if shoes_hypothesis <= shoes_premise:
    # check if the hypothesis value contradicts the estimate of more than 'shoes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shoes
    # any number of shoes greater than 'shoes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

