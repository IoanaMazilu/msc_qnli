tax_bill_premise = 27.5e9
sale_price_premise = 9.4e9
sale_price_hypothesis = 27.5e9

# the hypothesis talks about the sale price of Yuganskneftegaz, which is not mentioned in the premise
# the hypothesis cannot be entailed from the premise, since the sale price of Yuganskneftegaz is unknown.
label = "neutral"

print(label)
