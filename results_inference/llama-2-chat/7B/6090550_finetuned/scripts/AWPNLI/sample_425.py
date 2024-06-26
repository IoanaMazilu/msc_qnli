toys_cost_premise = 9.05
marbles_cost_premise = 9.05
football_cost_premise = 4.95
returned_baseball_money_premise = 6.52

toys_cost_hypothesis = 3.7

# the hypothesis refers to the total cost of toys, which is also mentioned in the premise
# compute the total cost of toys in the premise
toys_cost_premise = toys_cost_premise + marbles_cost_premise + football_cost_premise

if toys_cost_hypothesis!= toys_cost_premise:
    # check if the hypothesis value contradicts the total cost of toys in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(f"Toys cost: {toys_cost_premise}")
print(f"Hypothesis toys cost: {toys_cost_hypothesis}")
print(f"Label: {label}")
