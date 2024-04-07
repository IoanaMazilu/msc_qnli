# Premise: If Mary received $800 more than Harry did, what was the profit made by their business in that year?
# Hypothesis: If Mary received $more than 800 more than Harry did, what was the profit made by their business in that year?
# Golden Label: contradiction

mary_profit_more_than_harry_premise = 800
mary_profit_more_than_harry_hypothesis = 800

# the hypothesis refers to the profit difference between Mary and Harry mentioned in the premise
if mary_profit_more_than_harry_hypothesis != mary_profit_more_than_harry_premise:
    # check if the profit difference between Mary and Harry in the hypothesis contradicts the profit difference in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

