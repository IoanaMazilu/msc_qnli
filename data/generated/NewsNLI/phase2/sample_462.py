# Premise: The $35 million includes $2.5 million to pay legal fees and other expenses for the Nigerian government, Halliburton said.
# Hypothesis: The $35 million settlement includes Nigeria's legal fees and expenses.
# Golden Label: entailment

total_settlement_premise = 35000000
legal_fees_premise = 2500000

total_settlement_hypothesis = 35000000
# the hypothesis does not specify the amount dedicated to legal fees

# the hypothesis mentions the total amount of the settlement, which is also mentioned in the premise
# however, the hypothesis does not specify the amount for legal fees, which cannot be entailed from the premise
label = "neutral"

print(label)

