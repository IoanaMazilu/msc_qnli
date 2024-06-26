tax_bill_premise = 27.5e9
cost_premise = 9.4e9
cost_hypothesis = 27.5e9

# the hypothesis talks about the cost of Yuganskneftegaz, which is not explicitly mentioned in the premise
# the premise only mentions the sale price of Yuganskneftegaz, which is not the same as the cost
# the cost of Yuganskneftegaz is not mentioned in the premise, so we cannot infer entailment or contradiction
label = "neutral"

print(label)
