# Premise: The bank recently revised the charges to US Dollar 0.75 for every 3 transactions.
# Hypothesis: The bank recently revised the charges to US Dollar 0.75 for every less than 7 transactions.
# Golden Label: entailment

charges_per_transactions_premise = 0.75 / 3
charges_per_transactions_hypothesis = 0.75 / 7

# the hypothesis and the premise are referring to the charges for every transaction at the bank
if charges_per_transactions_premise < charges_per_transactions_hypothesis:
    # check if the charge per transaction in the hypothesis contradicts the charge per transaction in the premise
    label = "contradiction"
else:
    # if the charge per transaction in the hypothesis does not contradict the one in the premise
    # it means that the hypothesis can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)

