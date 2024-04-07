# Premise: If Matt has five iron coins and fiveteen copper coins, how many different sums from 1 ¢ to 160 ¢ can he make with a combination of his coins?
# Hypothesis: If Matt has five iron coins and fiveteen copper coins, how many different sums from less than 8 ¢ to 160 ¢ can he make with a combination of his coins?
# Golden Label: entailment

iron_coins_premise = 5
copper_coins_premise = 15
sum_premise_low = 1
sum_premise_high = 160

iron_coins_hypothesis = 5
copper_coins_hypothesis = 15
sum_hypothesis_low = 8
sum_hypothesis_high = 160

# Both the premise and hypothesis refer to the same number of iron and copper coins 
if iron_coins_premise != iron_coins_hypothesis or copper_coins_premise != copper_coins_hypothesis:
    # check if the number of iron or copper coins in the hypothesis contradicts the premise
    label = "contradiction"
elif sum_premise_low > sum_hypothesis_low or sum_premise_high != sum_hypothesis_high:
    # check if the range of sums in the hypothesis contradicts the range of sums in the premise
    label = "contradiction"
else:
    # if none of the values in the hypothesis contradict the premise, we can infer entailment
    label = "entailment"

print(label)

