# Premise: 2000 and Tony withdraws Rs.
# Hypothesis: less than 5000 and Tony withdraws Rs.
# Golden Label: entailment

withdrawn_amount_premise = 2000
withdrawn_amount_hypothesis = 5000

# the hypothesis refers to a withdrawal amount by Tony mentioned in the premise
if withdrawn_amount_premise >= withdrawn_amount_hypothesis:
    # check if the withdrawal amount in the premise contradicts the 'less than' estimate in the hypothesis
    label = "contradiction"
else:
    # any withdrawal amount less than 'withdrawn_amount_hypothesis' is consistent with the hypothesis
    # but it can't be explicitly entailed from the premise as the premise doesn't provide an upper boundary for the withdrawal amount
    label = "neutral"

print(label)

