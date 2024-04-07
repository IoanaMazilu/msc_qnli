# Premise: Marcella has less than 73 pairs of shoes.
# Hypothesis: Marcella has 23 pairs of shoes.
# Golden Label: neutral

shoes_premise = 73
shoes_hypothesis = 23

# the hypothesis talks about the number of shoes Marcella has, referenced also in the premise
if shoes_hypothesis >= shoes_premise:
    # check if the hypothesis value contradicts the estimate of less than 'shoes_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of shoes
    # any number of shoes less than 'shoes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

