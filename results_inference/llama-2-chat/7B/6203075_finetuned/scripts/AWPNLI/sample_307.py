candy_received_premise = 108.0
candy_eaten_premise = 36.0
candy_remaining_premise = candy_received_premise - candy_eaten_premise
piles_each_premise = 9.0
total_piles_hypothesis = candy_remaining_premise / piles_each_premise

# the hypothesis refers to the number of piles Sarah could make, which is calculated from the premise
# compute the total number of piles in the hypothesis
if total_piles_hypothesis!= candy_remaining_premise / piles_each_premise:
    # check if the number of piles in the hypothesis contradicts the number of piles in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
