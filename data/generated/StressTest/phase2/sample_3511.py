# Premise: If Matt has twu iron coins and twu copper coins, how many different sums from less than 8 ¢ to 14 ¢ can he make with a combination of his coins?
# Hypothesis: If Matt has twu iron coins and twu copper coins, how many different sums from 1 ¢ to 14 ¢ can he make with a combination of his coins?
# Golden Label: neutral

lower_sum_premise = 8
upper_sum_premise = 14
lower_sum_hypothesis = 1
upper_sum_hypothesis = 14

# the hypothesis and premise are talking about the range of sums Matt can make with his coins
# first we compare the lower bounds of the sum range
if lower_sum_hypothesis != lower_sum_premise:
    # if the lower bound of the sum range in the hypothesis contradicts that in the premise, we label it as a contradiction
    label = "contradiction"
# next we compare the upper bounds of the sum range
elif upper_sum_hypothesis != upper_sum_premise:
    # if the upper bound of the sum range in the hypothesis contradicts that in the premise, we label it as a contradiction
    label = "contradiction"
else:
    # if none of the bounds in the hypothesis contradict those in the premise, we have an entailment
    label = "entailment"

print(label)

