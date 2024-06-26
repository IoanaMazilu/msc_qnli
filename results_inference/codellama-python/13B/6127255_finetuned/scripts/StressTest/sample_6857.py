lowest_coin_value_premise = 1
highest_coin_value_premise = 35
lowest_coin_value_hypothesis = 2
highest_coin_value_hypothesis = 35

# the hypothesis refers to the range of coin values that Matt can make sums from, which is also mentioned in the premise
if lowest_coin_value_hypothesis < lowest_coin_value_premise or highest_coin_value_hypothesis > highest_coin_value_premise:
    # check if the range of coin values in the hypothesis contradicts the range of coin values in the premise
    label = "contradiction"
else:
    # if the range of coin values in the hypothesis does not contradict the range of coin values in the premise, we can infer entailment
    label = "entailment"

print(label)
