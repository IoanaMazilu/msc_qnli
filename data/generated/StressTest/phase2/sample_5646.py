# Premise: If Matt has ten iron coins and ten copper coins, how many different sums from 1 ¢ to 70 ¢ can he make with a combination of his coins?
# Hypothesis: If Matt has ten iron coins and ten copper coins, how many different sums from less than 7 ¢ to 70 ¢ can he make with a combination of his coins?
# Golden Label: entailment

iron_coins_premise = 10
copper_coins_premise = 10
sums_premise = (1, 70)

iron_coins_hypothesis = 10
copper_coins_hypothesis = 10
sums_hypothesis = (7, 70)

# the hypothesis refers to the number of iron and copper coins Matt has and the sum he can make with them, which is also mentioned in the premise
if iron_coins_premise != iron_coins_hypothesis or copper_coins_premise != copper_coins_hypothesis:
    # check if the number of iron and copper coins in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif sums_premise != sums_hypothesis:
    # check if the possible sums in the hypothesis contradicts the possible sums in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

