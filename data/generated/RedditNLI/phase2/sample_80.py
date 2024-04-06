# Premise: Coca-Cola expands into coffee with $5.1 billion deal for Britain's Costa.
# Hypothesis: Britain's Whitbread to sell Costa Coffee to Coke for $5.1 billion.
# Golden Label: neutral

deal_value_premise = 5.1
deal_value_hypothesis = 5.1

# the hypothesis and premise mention the deal value between Coca-Cola and Costa
if deal_value_hypothesis != deal_value_premise:
    # check if the deal value in the hypothesis contradicts the deal value in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

