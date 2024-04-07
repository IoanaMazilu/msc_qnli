# Premise: If Lary received $800 more than Terry did, what was the profit made by their business in that year?
# Hypothesis: If Lary received $more than 200 more than Terry did, what was the profit made by their business in that year?
# Golden Label: entailment

lary_profit_premise = 800
lary_profit_hypothesis = 200

# the hypothesis refers to the profit Lary made compared to Terry, as stated in the premise
if lary_profit_premise < lary_profit_hypothesis:
    # check if the profit Lary made in the hypothesis contradicts the profit Lary made in the premise
    label = "contradiction"
elif lary_profit_premise > lary_profit_hypothesis:
    # check if the profit Lary made in the hypothesis is less than the profit Lary made in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)

