# Premise: more than 1900 from Anwar at 6% p.
# Hypothesis: 3900 from Anwar at 6% p.
# Golden Label: neutral

amount_premise = 1900
amount_hypothesis = 3900
interest_rate = 6  # since the interest rate is the same in both premise and hypothesis, we don't need to compare it

# the hypothesis refers to the amount from Anwar mentioned in the premise
if amount_hypothesis <= amount_premise:
    # check if the amount in the hypothesis contradicts the estimate of more than 'amount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount
    # any amount greater than 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

