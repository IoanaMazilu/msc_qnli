coin_value_premise_min = 1
coin_value_hypothesis_min = 1
coin_value_premise_max = 35
coin_value_hypothesis_max = 35
coin_type_premise = 'iron'
coin_type_hypothesis = 'iron'
coin_count_premise = 5
coin_count_hypothesis = 5

# the hypothesis refers to the number and type of coins Matt has, which is also mentioned in the premise
if coin_count_hypothesis!= coin_count_premise:
    # check if the number of coins in the hypothesis contradicts the number of coins reported in the premise
    label = "contradiction"
elif coin_type_hypothesis!= coin_type_premise:
    # check if the type of coins in the hypothesis contradicts the type of coins reported in the premise
    label = "contradiction"
elif coin_value_hypothesis_min < coin_value_premise_min or coin_value_hypothesis_max!= coin_value_premise_max:
    # check if the range of coin values in the hypothesis contradicts the range of coin values reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
