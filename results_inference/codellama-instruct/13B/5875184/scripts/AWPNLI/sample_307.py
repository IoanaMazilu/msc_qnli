candy_received_premise = 108.0
candy_ate_premise = 36.0
candy_placed_premise = 9.0
candy_remaining_premise = candy_received_premise - candy_ate_premise
candy_per_pile_premise = candy_remaining_premise / 4.0

candy_per_pile_hypothesis = 9.0

if candy_per_pile_hypothesis > candy_per_pile_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
