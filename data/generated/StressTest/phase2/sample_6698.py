# Premise: 2000 and Tony withdraws Rs.
# Hypothesis: 7000 and Tony withdraws Rs.
# Golden Label: contradiction

withdrawn_amount_premise = 2000
withdrawn_amount_hypothesis = 7000

# the hypothesis talks about the amount withdrawn by Tony, which is also mentioned in the premise
if withdrawn_amount_hypothesis == withdrawn_amount_premise:
    # check if the value of 'withdrawn_amount_hypothesis' contradicts the value of 'withdrawn_amount_premise'
    label = "contradiction"
else:
    # the premise gives a specific amount for the withdrawn money
    # any other amount cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

