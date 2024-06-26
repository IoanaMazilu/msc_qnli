tax_bill_premise = 27.5e9
tax_bill_hypothesis = 27.5e9

# the hypothesis talks about the cost of Yuganskneftegaz which is not referenced in the premise (the cost of the company is not mentioned)
# the hypothesis cannot be entailed from the premise, since the cost of Yuganskneftegaz is unknown.
label = "neutral"

print(label)
