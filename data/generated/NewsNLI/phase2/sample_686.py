# Premise: The Taj Mahal, an Indian diamond and jade pendant sold for $8.8 million.
# Hypothesis: The Elizabeth Taylor diamond fetches $8.8 million.
# Golden Label: entailment

pendant_price_premise = 8.8
pendant_price_hypothesis = 8.8

# the hypothesis mentions the price of a diamond, which is also mentioned in the premise
# however, the hypothesis refers to the Elizabeth Taylor diamond, which cannot be entailed from the premise
label = "neutral"

print(label)

