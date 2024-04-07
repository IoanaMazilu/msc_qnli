# Premise: more than 2000 more and Bhavan withdraws Rs.
# Hypothesis: 4000 more and Bhavan withdraws Rs.
# Golden Label: neutral

withdraw_premise = 2000
withdraw_hypothesis = 4000

# the hypothesis refers to the amount Bhavan withdraws, also mentioned in the premise
if withdraw_hypothesis <= withdraw_premise:
    # check if the hypothesis value contradicts the estimate of more than 'withdraw_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount Bhavan withdraws
    # any amount greater than 'withdraw_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

