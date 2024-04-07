# Premise: John paid a 15% tip over the original price of the dish, while Jane paid the tip over the discounted price for the coupon.
# Hypothesis: John paid a less than 75% tip over the original price of the dish, while Jane paid the tip over the discounted price for the coupon.
# Golden Label: entailment

john_tip_premise = 15
john_tip_hypothesis = 75

# the hypothesis refers to the percentage tip paid by John over the original price of the dish 
if john_tip_hypothesis < john_tip_premise:
    # check if the hypothesis percentage contradicts the tip percentage paid by John in the premise
    label = "contradiction"
elif john_tip_hypothesis > john_tip_premise:
    # check if the hypothesis percentage contradicts the tip percentage paid by John in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

