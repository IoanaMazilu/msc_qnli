# Premise: The deal comes some two weeks after a $16 billion deal was reached between AT & T and SBC, a top rival for Qwest.
# Hypothesis: The two firms sealed the deal despite what was thought to be a higher offer from rival US carrier Qwest.
# Golden Label: neutral

deal_amount_premise = 16e9
deal_amount_hypothesis = 0 # the hypothesis does not mention a deal amount

# the hypothesis does not talk about the deal amount, which is the numerical information mentioned in the premise
# thus, the hypothesis cannot be entailed from the premise
label = "neutral"

print(label)

