# Premise: 4000 more and Bhavan withdraws Rs.
# Hypothesis: 8000 more and Bhavan withdraws Rs.
# Golden Label: contradiction

withdraw_premise = 4000
withdraw_hypothesis = 8000

# the hypothesis talks about the amount Bhavan withdraws, referenced also in the premise
if withdraw_hypothesis <= withdraw_premise:
    # check if the hypothesis value contradicts the estimate of more than 'withdraw_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the withdrawal amount
    # any withdrawal amount greater than 'withdraw_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

