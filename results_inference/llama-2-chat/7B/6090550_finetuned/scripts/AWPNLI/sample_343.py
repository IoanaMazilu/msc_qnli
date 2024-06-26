sacks_per_piece = 20.0
filled_sacks = 6.0
total_wood = 80.0

# the hypothesis refers to the number of filled sacks, which can be calculated from the premise
# compute the number of filled sacks in the premise
filled_sacks_premise = total_wood / sacks_per_piece
if filled_sacks_premise!= filled_sacks:
    # check if the number of filled sacks in the hypothesis contradicts the number of filled sacks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
