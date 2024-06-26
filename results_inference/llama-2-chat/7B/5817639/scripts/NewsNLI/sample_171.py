deal_premise = 0
deal_hypothesis = 300000000

# the hypothesis mentions the deal amount, which is also referenced in the premise
# however, the premise does not provide any information about the deal, so we cannot infer any relation
label = "neutral"

print(label)
