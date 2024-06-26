iron_coins_premise = 5
copper_coins_premise = 5
iron_coins_hypothesis = 5
copper_coins_hypothesis = 5

# the hypothesis talks about the number of coins Matt has, which is also mentioned in the premise
if iron_coins_hypothesis!= iron_coins_premise or copper_coins_hypothesis!= copper_coins_premise:
    # check if the number of coins in the hypothesis contradicts the number of coins in the premise
    label = "contradiction"
else:
    # if the number of coins in the hypothesis does not contradict the number of coins in the premise, we can infer entailment
    label = "entailment"

print(label)
