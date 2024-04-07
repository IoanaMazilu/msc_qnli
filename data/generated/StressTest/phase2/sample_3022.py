# Premise: John paid a less than 25% tip over the original price of the dish, while Jane paid the tip over the discounted price for the coupon.
# Hypothesis: John paid a 15% tip over the original price of the dish, while Jane paid the tip over the discounted price for the coupon.
# Golden Label: neutral

john_tip_premise = 25
john_tip_hypothesis = 15

# The hypothesis talks about the percentage of tip John and Jane paid which is also referenced in the premise
if john_tip_hypothesis > john_tip_premise:
    # check if the hypothesis value contradicts the estimate of less than 'john_tip_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the tip John paid
    # any percentage of tip less than 'john_tip_premise' is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)

