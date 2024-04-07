# Premise: If Sanoop returned 5 t-shirts to the retailer, and the average price of the remaining t-shirts was Rs.
# Hypothesis: If Sanoop returned 4 t-shirts to the retailer, and the average price of the remaining t-shirts was Rs.
# Golden Label: contradiction

returned_tshirts_premise = 5
returned_tshirts_hypothesis = 4

# the hypothesis refers to the number of returned t-shirts mentioned in the premise
if returned_tshirts_hypothesis != returned_tshirts_premise:
    # check if the hypothesis value contradicts the number of returned t-shirts in the premise
    label = "contradiction"
else:
    # no average price is mentioned in either the premise or hypothesis, so we cannot infer entailment or neutrality based on this information
    label = "neutral"

print(label)

