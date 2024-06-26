premise_coins = 2
hypothesis_coins = 3
iron_coins_premise = premise_coins * 2
iron_coins_hypothesis = hypothesis_coins * 2
copper_coins_premise = premise_coins * 5
copper_coins_hypothesis = hypothesis_coins * 5

# check if the hypothesis values and estimates do not contradict the premise ones
if iron_coins_hypothesis <= iron_coins_premise and copper_coins_hypothesis <= copper_coins_premise:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
elif iron_coins_hypothesis > iron_coins_premise or copper_coins_hypothesis > copper_coins_premise:
    # the hypothesis values contradict the premise ones, we can infer contradiction
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of coins, any number of coins less than 3 ¢ and 5 ¢ is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
