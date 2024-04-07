# Premise: John paid a 15% tip over the original price of the dish, while Jane paid the tip over the discounted price for the coupon.
# Hypothesis: John paid a less than 25% tip over the original price of the dish, while Jane paid the tip over the discounted price for the coupon.
# Golden Label: entailment

john_tip_premise = 15
john_tip_hypothesis = 25

# the hypothesis refers to the percentage of the tip John paid over the dish's price
if john_tip_premise >= john_tip_hypothesis:
    # check if the percentage of 'john_tip_hypothesis' contradicts the percentage of tip John paid in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

