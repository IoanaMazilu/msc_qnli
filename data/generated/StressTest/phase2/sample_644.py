# Premise: A shoe store sells Adidas shoes for $60 each and Puma shoes for $50 each.
# Hypothesis: A shoe store sells Adidas shoes for $10 each and Puma shoes for $50 each.
# Golden Label: contradiction

adidas_price_premise = 60
adidas_price_hypothesis = 10
puma_price_premise = 50
puma_price_hypothesis = 50

# the hypothesis refers to the selling prices of Adidas and Puma shoes stated in the premise
if adidas_price_premise != adidas_price_hypothesis:
    # check if the selling price of Adidas shoes in the hypothesis contradicts the selling price in the premise
    label = "contradiction"
elif puma_price_premise != puma_price_hypothesis:
    # check if the selling price of Puma shoes in the hypothesis contradicts the selling price in the premise
    label = "contradiction"
else:
    # if the hypothesis prices do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

