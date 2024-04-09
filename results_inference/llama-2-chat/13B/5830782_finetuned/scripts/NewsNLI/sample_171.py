deal_value_premise = 3e9
deal_value_hypothesis = 3e9

# the hypothesis mentions the deal value with Time Warner Cable, which is also referenced in the premise with Warners
# however, the companies are distinct and the deals are not the same, so we cannot infer entailment or contradiction
label = "neutral"

print(label)
