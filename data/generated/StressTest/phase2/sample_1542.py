# Premise: 3450 from Anwar at 6% p.
# Hypothesis: less than 5450 from Anwar at 6% p.
# Golden Label: entailment

amount_premise = 3450
amount_hypothesis = 5450

# the hypothesis talks about an amount from Anwar at a certain percentage, also mentioned in the premise
if amount_hypothesis <= amount_premise:
    # check if the hypothesis value contradicts the amount in the premise
    label = "contradiction"
elif amount_premise >= amount_hypothesis:
    # check if the amount in the premise contradicts the hypothesis value
    label = "contradiction"
else:
    # the premise gives a specific number for the amount
    # any number less than 'amount_hypothesis' is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

