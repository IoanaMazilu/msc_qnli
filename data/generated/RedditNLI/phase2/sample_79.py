# Premise: Britain's Whitbread to sell Costa Coffee to Coke for $5.1 billion.
# Hypothesis: Coca-Cola expands into coffee with $5.1 billion deal for Britain's Costa.
# Golden Label: entailment

price_premise = 5.1
price_hypothesis = 5.1

# the hypothesis and premise mention the price of the deal
if price_premise != price_hypothesis:
    # check if the price in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

