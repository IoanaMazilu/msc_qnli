# Premise: John paid a 15% tip over the original price of the dish, while Jane paid the tip over the discounted price for the coupon.
# Hypothesis: John paid a 55% tip over the original price of the dish, while Jane paid the tip over the discounted price for the coupon.
# Golden Label: contradiction

tip_rate_john_premise = 15
tip_rate_john_hypothesis = 55

# the hypothesis refers to the tip rate paid by John, mentioned also in the premise
if tip_rate_john_hypothesis != tip_rate_john_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate reported in the premise
    label = "contradiction"
else:
    # the premise and the hypothesis are consistent regarding Jane's tip payment
    # if the tip rate for John in the hypothesis and the premise are the same, we can infer entailment
    label = "entailment"

print(label)

