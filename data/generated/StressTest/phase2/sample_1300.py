# Premise: more than 3050 from Anwar at 6% p.
# Hypothesis: 4050 from Anwar at 6% p.
# Golden Label: neutral

amount_premise = 3050
amount_hypothesis = 4050

# the hypothesis refers to an amount from Anwar mentioned in the premise
if amount_hypothesis <= amount_premise:
    # check if the amount in the hypothesis contradicts the estimate of more than 'amount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount
    # any amount greater than 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

