# Premise: If Matt has five iron coins and ten copper coins, how many different sums from less than 3 ¢ to 60 ¢ can he make with a combination of his coins?
# Hypothesis: If Matt has five iron coins and ten copper coins, how many different sums from 1 ¢ to 60 ¢ can he make with a combination of his coins?
# Golden Label: neutral

iron_coins_premise = 5
copper_coins_premise = 10
sum_lower_limit_premise = 3
sum_upper_limit_premise = 60

iron_coins_hypothesis = 5
copper_coins_hypothesis = 10
sum_lower_limit_hypothesis = 1
sum_upper_limit_hypothesis = 60

# the hypothesis refers to the number of iron coins, copper coins and possible sums mentioned in the premise
if iron_coins_premise != iron_coins_hypothesis or copper_coins_premise != copper_coins_hypothesis:
    # check if the number of coins in the hypothesis contradicts the number of coins in the premise
    label = "contradiction"
elif sum_upper_limit_hypothesis != sum_upper_limit_premise:
    # check if the upper limit of the sum in the hypothesis contradicts the upper limit of the sum in the premise
    label = "contradiction"
elif sum_lower_limit_hypothesis >= sum_lower_limit_premise:
    # check if the lower limit of the sum in the hypothesis contradicts the lower limit of the sum in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

